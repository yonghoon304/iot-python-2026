# 구구단

# 2중 for문

dan = int(input("출력 최대 단 수 > "))

for i in range(2,dan+1):
    print(f"{i}단 출력")

    for j in range(2,10):
        print(f"{i}*{j}= {i*j:>2} ",end="")

