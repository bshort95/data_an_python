import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

dt1 = pd.read_csv('2015.csv')
dt2 = pd.read_csv('2016.csv')
dt3 = pd.read_csv('2017.csv')
dt4 = pd.read_csv('2018.csv')
dt5 = pd.read_csv('2019.csv')

america_total = pd.DataFrame()
america_total['year'] = 0
america_total['rank'] = 0
america_total['score'] = 0
america_total['gdp'] = 0
america_total['freedom'] = 0

world_total = pd.DataFrame()
world_total['country'] = 0
world_total['year'] = 0
world_total['total score'] = 0

d1 = {
    "year": 2015,
    "rank": dt1.iloc[14,2],
    "score": dt1.iloc[14,3],
    'gdp': dt1.iloc[14,5],
    'freedom': dt1.iloc[14,8]

}

temp1 = pd.DataFrame(data = d1, index = [0])
america_total = america_total.append(temp1)

d2 = {
    "year": 2016,
    "rank": dt2.iloc[12,2],
    "score": dt2.iloc[12,3],
    'gdp': dt2.iloc[12,6],
    'freedom': dt2.iloc[12,9]

}

temp2 = pd.DataFrame(data = d2, index = [1])
america_total = america_total.append(temp2)

d3 = {
    "year": 2017,
    "rank": dt3.iloc[13,1],
    "score": dt3.iloc[13,2],
    'gdp': dt3.iloc[13,5],
    'freedom': dt3.iloc[13,8]

}

temp3 = pd.DataFrame(data = d3, index = [2])
america_total = america_total.append(temp3)

d4 = {
    "year": 2018,
    "rank": dt4.iloc[17,0],
    "score": dt4.iloc[17,2],
    'gdp': dt4.iloc[17,3],
    'freedom': dt4.iloc[17,6]

}

temp4 = pd.DataFrame(data = d4, index = [3])
america_total = america_total.append(temp4)

d5 = {
    "year": 2019,
    "rank": dt5.iloc[18,0],
    "score": dt5.iloc[18,2],
    'gdp': dt5.iloc[18,3],
    'freedom': dt5.iloc[18,6]

}


temp5 = pd.DataFrame(data = d5, index = [4])
america_total = america_total.append(temp5)

fig, axis1 = plt.subplots()


axis1.plot(america_total['year'],america_total['score'], label = "score")

axis2 = axis1.twinx()
axis1.set_ylabel('Scores')
axis1.set_xlabel('year')
axis2.set_ylabel('peoples perception of gdp')
axis1.set_title('United states happiness scores compared to peoples perception of gdp')


axis2.plot(america_total['year'],america_total['gdp'], color = 'r', label = "gdp", linestyle='--')

plt.xticks([2015,2016,2017,2018,2019])

lines = axis1.get_lines() + axis2.get_lines()


plt.legend(lines, [l.get_label() for l in lines], loc='upper right')


plt.show()

fig, ax = plt.subplots()
dt1 = dt1.sort_values('Region')
plt.barh(dt1['Region'],dt1['Happiness Score'], color = "r")
ax.set_xlabel('hapiness score')
ax.set_title('happiness score by region')



plt.show()


