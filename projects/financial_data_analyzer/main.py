import csv

total_sales = 0

with open("sample_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:  
        total_sales += int(row["매출"])

print("총매출 : ", total_sales)

