The assumptions of the linear regression line (after taking logarithm of both the volume and the IC50 values) of [Figure 12](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/figure12.pdf) are tested graphically in this ![figure](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/linear_regression_test.png).
This figure was generated using the script [regression_test.py](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/regression_test.py).
The assumptions are discussed below:
1. Homoscedasticity: Subplot 1 (left) shows that there the residuals are randomly distributed about the y = 0 line indicating that the variance is not dependent on the level of the predicted value.
2. Normal distribution: Subplot 2 (centre) shows that the quantile-quantile plot falls roughly on a 45&deg; angle indicating a normal distribution of the residuals.
3. Independence of datapoints: Subplot 1 (left) and subplot 3 (right) show that there is no discernible pattern of the residuals with respect to either the predicted value or the independent variable.
