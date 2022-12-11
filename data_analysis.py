import pandas as pd

#데이터 불러오기
filePath = 'A회사_보습제_매출데이터_v1.csv'

salesData = pd.read_csv(filePath, encoding = 'cp949')

salesData = salesData.transpose()
salesData.rename(columns = salesData.iloc[0], inplace = True)
salesData = salesData.drop(salesData.index[0])

salesData

import re

# 특수기호 제거
for col in list(salesData.columns):
    refineded = []
    for x in list(salesData[col]):
        try:
            refineded.append(int(re.sub(r"[^0-9.]", "", x)))
        except:
            refineded.append(float(re.sub(r"[^0-9.]", "", x)))
    salesData[col] = refineded
    
salesData

import matplotlib.pyplot as plt

# 이전 과제 

totalSales = list(salesData['총매출'])
unitPrices = list(salesData['1온스별단가'])
salesVolumes = []

for idx in range(len(totalSales)):
    volume = round(totalSales[idx] / unitPrices[idx])
    salesVolumes.append(volume)
    
advPrice = list(salesData['광고비용'])
months = list(salesData.index)

plt.style.use('default')
plt.rcParams['font.size'] = 12

fig, ax1 = plt.subplots()
ax1.plot(months, salesVolumes, color='green')
ax1.set_ylabel('salesVolumes')
ax1.grid(True, axis = 'y')

plt.ylim(2400000, 3200000)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['$' + '{:,.0f}'.format(x) for x in current_values])

ax2 = ax1.twinx()
ax2.set_ylabel('advPrice')
ax2.plot(months, advPrice, color='deeppink')

plt.ylim(0, 1200000)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['$' + '{:,.0f}'.format(x) for x in current_values])

plt.show()