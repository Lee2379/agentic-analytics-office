# Executive analytics report

## Decision summary

The synthetic portfolio contains 15 products with a median price of KRW 21,900. The chronological baseline achieved holdout MAE 2.38 units and projects 274 units over seven days.

## Data quality

- Valid product records: 15
- Valid chronological sales days: 35
- Duplicate product IDs: 0
- Duplicate dates: 0
- QA status: **passed**

## Market snapshot

- Average price: KRW 22,767
- Median price: KRW 21,900
- Discounted share: 93.3%
- Average discount across all products: 17.9%
- Review-weighted rating: 4.23/5
- Available stock: 486 units

## Forecast evaluation

- Training observations: 28
- Holdout observations: 7
- Train end: 2026-06-28
- Holdout start: 2026-06-29
- MAE: 2.38 units
- RMSE: 2.77 units
- MAPE: 6.95%
- Seven-day projected demand: 274 units

## Decision notes

- The training-window trend is increasing at 0.47 units per day.
- Discounting is widespread in the synthetic assortment; margin impact should be reviewed before expanding promotions.
- Review-weighted customer feedback is strong in the synthetic sample.
- The baseline projects approximately 274 units over the next seven days.

## Limitations

- All demo data is synthetic and supports engineering evaluation, not a real commercial decision.
- Linear trend is an interpretable baseline and does not model seasonality or promotions.
- Holdout metrics are based on seven observations and should not be over-generalized.
- The deterministic harness validates contracts; it does not reproduce private LLM reasoning.
