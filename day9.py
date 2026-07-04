with open("sales.csv", "r", encoding="utf-8") as file:
    next(file)
    
    for line in file:
        data = line.strip().split(",")

        print("회사명:", data[0])
        print("매출액:", data[1])
        print("영업이익:", data[2])
        

        sales = int(data[1])
        profit = int(data[2])
        rate = profit / sales * 100

        print(f"영업이익률: {rate:.2f}%")
        print("-----------------")
        