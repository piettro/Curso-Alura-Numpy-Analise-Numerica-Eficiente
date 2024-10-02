import numpy as np
import matplotlib.pyplot as plt

url = './Data/apples_ts.csv'
data = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

data_transpose = data.T
dates = np.arange(1, 88)
prices = data_transpose[:,1:6]
prices_moscow = prices[:,0]

x = dates
y = 2 * x + 80

plt.plot(x, prices_moscow)
plt.plot(x, y)
plt.show()

print(np.sqrt(np.sum(np.power(prices_moscow - y,2))))

x = dates
y = 0.52 * x + 80

plt.plot(x, prices_moscow)
plt.plot(x, y)
plt.show()

print(np.sqrt(np.sum(np.power(prices_moscow - y,2))))

print(np.linalg.norm(prices_moscow-y))

Y = prices_moscow
X = dates
n = np.size(prices_moscow)
coef_ang = (n * np.sum(X*Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np. sum(X)**2)
coef_lin = np.mean(Y) - coef_ang * np.mean(X)
print(coef_ang, coef_lin)

y = coef_ang * X + coef_lin
print(np.linalg.norm(prices_moscow-y))
plt.plot(x, prices_moscow)
plt.plot(x, y)
plt.show()