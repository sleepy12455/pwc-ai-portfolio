from analyzer import (
    calculate_average_profit,
    calculate_total_sales,
    find_best_company
)


    
print("=============================")
print("Financial Data Analyzer")
print("=============================")

filename = input("분석할 CSV 파일명을 입력하세요: ").strip()


try:

    print ("총매출: ", calculate_total_sales(filename))
    print ("평균 영업이익: ", calculate_average_profit(filename))
    print("최고 매출 기업:", find_best_company(filename))

except FileNotFoundError:
    print("CSV 파일을 찾을 수 없습니다.")
    