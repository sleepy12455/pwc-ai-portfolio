import csv

def calculate_total_sales(filename):
    total_sales = 0

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total_sales += int(row["매출"])

        return total_sales

def calculate_average_profit(filename):
    total_profit = 0
    count = 0

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_profit += int(row["영업이익"])
            count += 1
        
        return total_profit / count
    
print("=============================")
print("Financial Data Analyzer")
print("=============================")

print ("총매출: ", calculate_total_sales("sample_data.csv"))
print ("평균 영업이익: ", calculate_average_profit("sample_data.csv"))

def find_best_company(filename):
    best_company = ""
    highest_sales = 0

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sales = int(row["매출"])

            if sales > highest_sales:
                highest_sales = sales
                best_company = row["회사"]

            return best_company

print("최고 매출 기업:", find_best_company("sample_data.csv"))
