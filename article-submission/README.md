# Article submission content

Branch `article-submission-content` holds the material for the article planned for this product. The product code on the default branch is unchanged.

| Item | Value |
|------|-------|
| Target venue | IAI2027 – 9th International Conference on Industrial AI |
| Type | conf |
| Deadline | 2026-12-31 – چکیده تا ۳۱ اکتبر ۲۰۲۶؛ ارسال تا ۳۱ دسامبر ۲۰۲۶ |
| Official page | https://easychair.org/cfp/iai2027 |
| Abstract rule (Springer / EasyChair conference) | Single paragraph of 150–250 words, written for the full-paper track; 3–5 keywords. Typical length 150–250 words; keywords 3–5. |

## Title
A Digital Twin with Soft Sensors for Grade-Transition Optimisation and Catalyst Degradation Prediction in a Petrochemical Plant

## Abstract (draft)
Polyolefin plants switch between product grades several times a year, and each transition produces off-specification material while laboratory results for melt flow index (MFI) and density arrive hours late. This paper presents a digital twin for a petrochemical production line that combines soft sensors with transition-sequence optimisation and degradation forecasting. Soft sensors estimate MFI and density online from process measurements read from the distributed control system through OPC-UA. An optimiser then orders grade changes and proposes transition trajectories that shorten the off-specification period, and a separate model forecasts catalyst degradation and reactor fouling to support maintenance planning. The twin was developed with operating data from [plant, period] covering [N] grade transitions. The soft sensors achieved an error of [X] for MFI and [Y] for density against laboratory values. In replay of historical campaigns, the optimised sequence reduced estimated off-specification production by [Z]% relative to the actual sequence, and the degradation model gave [W] weeks of warning before the planned catalyst change. The results suggest that industrial AI built around a digital twin can turn delayed laboratory feedback into actionable guidance for operators, and the paper discusses requirements for deployment in closed-loop operation.

**Keywords:** digital twin; soft sensor; grade transition; petrochemical; predictive maintenance

## Before submitting
1. Replace every `[bracketed]` placeholder with values measured by the team on real data; no number in the draft is a result.
2. Add author names and affiliations; confirm the abstract limits in the venue's author guidelines (the limits above are typical for the venue family).
3. Add the experiment scripts and data description used for the results to this branch.
4. The Word file for the submission system is prepared in the platform repository (`outputs/abstracts/`).
