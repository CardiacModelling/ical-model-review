import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

import statsmodels.api as sm

# load data
data = pd.read_csv('ic50.csv', usecols=['x', 'y'])
data = data.sort_values('x')
vol = data['x'].to_numpy()
ic50 = data['y'].to_numpy()
vol = np.log(vol)
ic50 = np.log(ic50)
vol_fit = vol.reshape((-1, 1))


model = LinearRegression().fit(vol_fit, ic50)

r_sq = model.score(vol_fit, ic50)
c = model.intercept_
m = model.coef_
m = m[0]

pred = m*vol + c
res = ic50 - pred

fig = plt.figure(figsize=(6.6, 3))
ax1 = fig.add_subplot(131)

### Does not make sense for non-time series data
# res_data = pd.DataFrame(res)
# pd.plotting.autocorrelation_plot(res_data)
# plt.grid('off')
# plt.show()

# residuals: independent (non-random pattern around 0), 
# residuals: homoscodasticity (variance does not depend on the magnitude of prediction)
ax1.scatter(pred, res)
ax1.axhline(y=0, color = 'red')
ax1.set_xlabel('Predicted value of IC50')
ax1.set_ylabel('Residual')



# normality: 
# qq plot should fall on 45 degree angle
ax2 = fig.add_subplot(133)
sm.qqplot(res, line='45', ax = ax2, fit = True)
ax2.get_lines()[0].set_markerfacecolor('#1f77b4')
ax2.get_lines()[0].set_markeredgecolor('#1f77b4')
ax2.set_ylabel('Sample Quantile')
ax2.set_xlabel('Theoretical Quantile')
ax2.set_title('')

# independence wrt to the independent variabele vol
ax3 = fig.add_subplot(132)
ax3.scatter(vol, res)
ax3.set_xlabel('Volume')
ax3.set_ylabel('Residual')
ax3.axhline(y=0, color = 'red')

plt.tight_layout()
plt.savefig('linear_regression_test.png')
plt.close()

