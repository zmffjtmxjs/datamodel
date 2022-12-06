import pandas as pd


#데이터 불러오기
filePath = 'A회사_보습제_매출데이터_v1.csv'

salesData = pd.read_csv(filePath, encoding = 'cp949')

salesData = salesData.transpose()
salesData.rename(columns = salesData.iloc[0], inplace = True)
salesData = salesData.drop(salesData.index[0])
salesData

#데이터 전처리
import re

for col in list(salesData.columns):
    repl = []
    for x in list(salesData[col]):
        try:
            repl.append(int(re.sub(r"[^0-9.]", "", x)))
        except:
            repl.append(float(re.sub(r"[^0-9.]", "", x)))
    salesData[col] = repl
    
salesData


