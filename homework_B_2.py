x = int(input("行数を入力してください:"))
y = int(input("列数を入力してください:"))

for n in range(1, x + 1):
    for s in range(1, y + 1):
        print(n * s, end=" ")
    print()
