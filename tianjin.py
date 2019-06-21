import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime

data = pd.read_csv("tj.csv")
data.year_months = [datetime.strptime(d, '%b-%y') for d in data.year_months]
data = data.sort_values(by='year_months')

GDP = pd.read_csv("GDP.csv", dtype={'year': 'object'})
GDP.year = [datetime.strptime(d, '%y') for d in GDP.year]

M2 = pd.read_csv("M2.csv", dtype={'year': 'object'})
M2.year = [datetime.strptime(d, '%y') for d in M2.year]

fig, ax = plt.subplots(figsize=(20, 6))

ax.plot(data.year_months.values, data.avg_price.values, label='avg_price')
ax.plot(GDP.year.values, GDP.GDP.values/(GDP.GDP[0]/data.avg_price[0]), '--', label='GDP')
ax.plot(M2.year.values, M2.M2.values/(M2.M2[0]/data.avg_price[0]), '--', label='M2')


ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())

ax.set_title('tianjin house avg_price and influence factor')
ax.legend()

fig.savefig("tj.png")
plt.show()