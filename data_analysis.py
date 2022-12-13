# 데이터 불러오기
def load_data(file_path):
    import pandas as pd
    
    data = pd.read_csv(file_path, encoding = 'cp949')

    data = data.transpose()
    data.rename(columns = data.iloc[0], inplace = True)
    data = data.drop(data.index[0])

    return data

# 특수문자 제거하기
def refined_data(df):
    import re
    
    for col in list(df.columns):
        refineded = []
        for x in list(df[col]):
            try:
                refineded.append(int(re.sub(r"[^0-9.%:]", "", x)))
            except:
                try:
                    refineded.append(float(re.sub(r"[^0-9.%:]", "", x)))
                except:
                    refineded.append(str(re.sub(r"[^0-9.%:]", "", x)))
        df[col] = refineded
    
    return df

#=============================================================================================

# 데이터 불러오기
salesData = load_data('A회사_보습제_매출데이터_v1.csv')
salesData

# 데이터 전처리
salesData = refined_data(salesData)
salesData

import matplotlib.pyplot as plt

# 이전 과제에서 작성한 그래프를 파이썬으로 구현

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


# 데이터 불러오기
salesData = load_data('A회사_보습제_매출데이터_v1_edited.csv')
salesData

# 데이터 전처리
salesData = refined_data(salesData)
salesData

# 판매 갯수 구하기
salesVolumes = []
for x, y in zip(list(salesData['총매출']), list(salesData['병당 가격'])):
    salesVolumes.append(x // y)
    
salesVolumes

# 순이익 구하기
netProfit = []
for x, y in zip(list(salesData['이익']), salesVolumes):
    netProfit.append(x * y)
    
netProfit

# 판매량과 순이익 그래프 그리기
months = list(salesData.index)

plt.style.use('default')
plt.rcParams['font.size'] = 12

fig, ax1 = plt.subplots()
ax1.plot(months, salesVolumes, color='green')
ax1.set_ylabel('salesVolumes(green)')
ax1.grid(True, axis = 'y')

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

ax2 = ax1.twinx()
ax2.set_ylabel('netProfit(pink)')
ax2.plot(months, netProfit, color='deeppink')

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['$' + '{:,.0f}'.format(x) for x in current_values])

plt.show()

# 제조원가에 따른 총 순이익 변화
import numpy as np

x = np.arange(3, 6, 0.01)
y = (7.60 - 1.28 - x) * salesVolumes[-1]

plt.plot(x, y)
plt.ylim(2000000, 10000000)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['$' + '{:,.0f}'.format(x) for x in current_values])

plt.grid(True)
plt.axvline(5.12, 0, 1, color = 'red', linestyle = '--')

for idx in reversed(range(len(x))):
    if y[idx] > 6476000:
        recommandCost = x[idx]
        break

plt.axvline(recommandCost, 0, 1, color = 'green', linestyle = '--')

plt.show()