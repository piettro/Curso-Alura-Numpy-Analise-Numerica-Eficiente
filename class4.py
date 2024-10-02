import numpy as np

url = './Data/apples_ts.csv'
data = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

data_transpose = data.T
dates = np.arange(1, 88)
prices = data_transpose[:,1:6]
prices_moscow = prices[:,0]

Y = prices_moscow
X = dates
n = np.size(prices_moscow)
coef_ang = (n * np.sum(X*Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np. sum(X)**2)
coef_lin = np.mean(Y) - coef_ang * np.mean(X)

np.random.seed(84)
np.random.randint(low=40,high=100,size=100)
coef_angulares = np.random.uniform(low=0.10,high=0.90,size=100)

for i in range(100):
    print(np.linalg.norm(prices_moscow-(coef_angulares[i]*X+coef_lin)))

norm2 = np.array([])

for i in range(100):
    norm2 = np.append(norm2, np.linalg.norm(prices_moscow-(coef_angulares[i]*X+coef_lin)))

print(norm2)