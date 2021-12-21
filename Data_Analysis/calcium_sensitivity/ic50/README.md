The assumptions of the linear regression line (after taking logarithm of both the volume and the IC50 values) of [Figure 12](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/figure12.pdf) are tested graphically in the figure below:

![figure](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/linear_regression_test.png)

This figure was generated using the script [regression_test.py](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/regression_test.py).
The assumptions are discussed below:
1. Homoscedasticity: Subplot 1 (left) the residuals (data points minus the regression line) appear to be randomly distributed around y = 0, suggesting that the variance is not dependent on the level of the predicted value.
2. Independence of datapoints: Subplot 1 (left) and subplot 2 (centre) show that there is no discernible pattern of the residuals with respect to either the predicted value or the independent variable.
3. Normal distribution: Subplot 3 (right) shows that the quantile-quantile plot falls roughly on a 45&deg; angle indicating a normal distribution of the residuals. Please note that these quantiles are formed from the standardised normalised dataset used for the calculation of theoretical quantiles. 
