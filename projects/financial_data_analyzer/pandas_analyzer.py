import pandas as pd 

filename = input("분석할 CSV 파일명을 입력하세요: ").strip()

df = pd.read_csv(filename)

print("====================")
print("Financial Data Analyzer (Pandas)")
print("====================")

print("총매출 :", df["매출"].sum())

print("평균 영업이익 :", df["영업이익"].mean())

best_company = df.loc[df["매출"].idxmax()]

print("최고 매출 기업 :", best_company["회사"])

print(df.describe())
