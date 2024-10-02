import numpy as np

url = './Data/apples_ts.csv'
data = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))
data_transpose = data.T
print(data_transpose)

print(f'Ndim: {data_transpose.ndim}')
print(f'Size: {data_transpose.size}')
print(f'Shape: {data_transpose.shape}')


