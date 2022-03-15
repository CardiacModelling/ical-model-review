import pandas as pd

data = pd.read_csv('ic50.csv')
ic50 = data['y']
print('min: ', ic50.min())
print('max: ', ic50.max())
print('median: ', ic50.median())
print('mean: ', ic50.mean())
print('quantile 90: ', ic50.quantile(0.9))
print('quantile 10: ', ic50.quantile(0.1))