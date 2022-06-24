users = ["Bob", "Tom", "Ken"]  # A-1

int_numbers = [1, 2, 3, 4, 5]  # A-2

bob_info = ["Bob", "Dylan", 79]  # A-3

members = ["Bob", "Tom", "Ken"]  # A-4
print(members[0])
print(members[1])

bob_info = ["Bob", "Dylan", 79]  # A-5
print("Name:{}".format(bob_info[0]))
print((bob_info[1]))
print("Age:{}".format(bob_info[2]))

odd_numbers = [1, 3, 5, 7, 9]  # A-6
for number in odd_numbers:
    print(number)

even_numbers = [2, 4, 6, 8]  # A-7
twice_numbers = []
for even_number in even_numbers:
    twice_numbers.append(int(even_number) * 2)

print(twice_numbers)

users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]  # A-8
print("Name:" + users_info[0][0] + ",Age:" + str(users_info[0][1]))
print("Name:" + users_info[1][0] + ",Age:" + str(users_info[1][1]))
print("Name:" + users_info[2][0] + ",Age:" + str(users_info[2][1]))

bob_info = {"first_name": "Bob", "family_name": "Dylan", "age": 79}  # A-9
print(bob_info["first_name"])  # "Bob"
print(bob_info["family_name"])  # "Dylan"
print(bob_info["age"])  # 79

import random


def dice():
    return random.randint(1, 6)


print(dice())  # 1から6の整数をランダムに出力する
