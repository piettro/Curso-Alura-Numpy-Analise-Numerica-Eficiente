import numpy as np
import matplotlib.pyplot as plt

url = './Data/apples_ts.csv'
data = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

data_transpose = data.T
dates = np.arange(1, 88)
prices = data_transpose[:,1:6]
prices_moscow = prices[:,0]
prices_kaliningrad = prices[:,1]
prices_petersburg = prices[:,2]
prices_krasnodar = prices[:,3]
prices_ekaterinburg = prices[:,4]

moscow_year1 = prices_moscow[0:12] 
moscow_year2 = prices_moscow[12:24]
moscow_year3 = prices_moscow[24:36]
moscow_year4 = prices_moscow[36:48]

plt.plot(dates,prices_moscow)
plt.show()

plt.plot(np.arange(1,13,1),moscow_year1)
plt.plot(np.arange(1,13,1),moscow_year2)
plt.plot(np.arange(1,13,1),moscow_year3)
plt.plot(np.arange(1,13,1),moscow_year4)
plt.legend(['Year1','Year2','Year3','Year4'])
plt.show()

result = np.array_equal(moscow_year3,moscow_year4)
print(result)

result = np.allclose(moscow_year3,moscow_year4,10)
print(result)

result_nan = sum(np.isnan(prices_kaliningrad))
print(result_nan)