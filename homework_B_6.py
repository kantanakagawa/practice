"""
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること
"""
import random

N = int(input("サイコロの面の数は?:"))
M = int(input("何回振りますか?: "))

numbers_list = list()

for r in range(0, M):

    dice = random.randint(1, N)
    numbers_list.append(dice)

print(numbers_list)
