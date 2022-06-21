numbers = input(("データを入力してください(スペース区切り) > ")).split()

sum_number = 0
for r in range(0, len(numbers)):
    number = int(numbers[r])
    sum_number += number

print(f"合計値: {sum_number}")


maxnumber = numbers[0]

for i in range(0, len(numbers)):
    if numbers[i] > maxnumber:
        maxnumber = numbers[i]

print(f"最大値：{maxnumber}")

minnumber = numbers[0]
for i in range(0, len(numbers)):
    if numbers[i] < minnumber:
        minnumber = numbers[i]

print(f"最小値：{minnumber}")


average = sum_number / len(numbers)
print(f"平均値: {average}")
