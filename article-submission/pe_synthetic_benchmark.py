import json,numpy as np,pandas as pd
from ampt import simulator as sim, virtual_sensor as vs
def run(seed,lab_every=480,delay=120):
    df=sim.simulate(20000,seed=seed)
    n=len(df);grades=sorted(df.grade.unique());rng=np.random.default_rng(seed)
    test_g=set(rng.choice(grades,size=len(grades)//3,replace=False))
    tr=df[(~df.grade.isin(test_g))&(df.minutes_since_change>250)]
    s=vs.VirtualSensor().fit(tr.h2_ratio,tr.comonomer_ratio,tr.mfi,tr.density)
    hat,_=s.predict(df.h2_ratio,df.comonomer_ratio)
    # lab: sample taken every lab_every min, result available delay min later
    avail=np.full(n,np.nan);lastsame=np.full(n,np.nan);hist={}
    cur=np.nan
    results=[(t+delay,t) for t in range(0,n,lab_every) if t+delay<n]
    ri=0;cur=np.nan;lastg={}
    for i in range(n):
        while ri<len(results) and results[ri][0]==i:
            t=results[ri][1];cur=df.mfi.iat[t];lastg[df.grade.iat[t]]=cur;ri+=1
        avail[i]=cur
        lastsame[i]=lastg.get(df.grade.iat[i],np.nan)
    d=df.assign(vs=hat,lab_last=avail,lab_same=lastsame)
    d=d[d.grade.isin(test_g)&d.lab_last.notna()]
    out={}
    for nm,msk in [("all",d.minutes_since_change>=0),("transition",d.minutes_since_change<250),("steady",d.minutes_since_change>=250)]:
        x=d[msk]
        r={}
        for m in ["vs","lab_last","lab_same"]:
            y=x[m];ok=y.notna()
            r[m]={"rmse_log":float(np.sqrt(np.mean((np.log(y[ok])-np.log(x.mfi[ok]))**2))),"mape":float(np.mean(np.abs((y[ok]-x.mfi[ok])/x.mfi[ok]))),"n":int(ok.sum())}
        y=x[x.lab_same.notna()];r["vs_on_same"]={"rmse_log":float(np.sqrt(np.mean((np.log(y.vs)-np.log(y.mfi))**2))),"mape":float(np.mean(np.abs((y.vs-y.mfi)/y.mfi))),"n":int(len(y))}
        out[nm]=r
    return out
res=[run(s) for s in range(20)]
agg={}
for nm in ["all","transition","steady"]:
    agg[nm]={}
    for m in ["vs","lab_last","lab_same","vs_on_same"]:
        for k in ["rmse_log","mape","n"]:
            v=np.array([r[nm][m][k] for r in res]);agg[nm].setdefault(m,{})[k]=[float(v.mean()),float(1.96*v.std(ddof=1)/np.sqrt(len(v)))]
    v=np.array([r[nm]["vs"]["rmse_log"]<r[nm]["lab_last"]["rmse_log"] for r in res]);agg[nm]["vs_beats_lab_last"]=float(v.mean())
    v=np.array([r[nm]["vs_on_same"]["rmse_log"]<r[nm]["lab_same"]["rmse_log"] for r in res]);agg[nm]["vs_beats_lab_same"]=float(v.mean())
json.dump(agg,open("pe_res.json","w"),indent=1);print(json.dumps(agg,indent=1))
