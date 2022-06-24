def sum():
    sum_number = 0

    for r in range(0, len(numbers)):
        number = int(numbers[r])
        sum_number += number

    return sum_number


def max():
    max_number = 0

    for r in range(0, len(numbers)):
        num = int(numbers[r])
        if num > max_number:
            max_number = num

    return max_number


def min():
    min = 0

    for r in range(0, len(numbers)):
        if numbers[min] > numbers[r]:
            min = r

    return numbers[min]


def average():

    average = int(sum() / len(numbers))
    return average


# function
if __name__ == "__main__":
    # リスト
    numbers = input(("データを入力してください(スペース区切り) > ")).split()

    print(f"合計値： {sum()}")
    print(f"最大値： {max()}")
    print(f"最小値： {min()}")
    print(f"平均値： {average()}")
