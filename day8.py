with open("introduce.txt", "w", encoding="utf-8") as file:
    file.write("이름: 승욱\n")
    file.write("목표: 회계법인 AI 취업")

with open("introduce.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)

print("----- 한 줄씩 출력 -----")

with open("introduce.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
        