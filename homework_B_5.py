numbers = input(("データを入力してください(スペース区切り) > ")).split()


def sum():
    sum_number = 0
    for r in range(0, len(numbers)):
        number = int(numbers[r])
        sum_number += number
        return sum_number


def max():
    maxnumber = numbers[0]
    for i in range(0, len(numbers)):
        if numbers[i] > maxnumber:
            maxnumber = numbers[i]
        return maxnumber


def min():
    minnumber = numbers[0]
    for i in range(0, len(numbers)):
        if numbers[i] < minnumber:
            minnumber = numbers[i]
        return minnumber


def average():

    average = int(sum() / len(numbers))
    return average


if __name__ == "__main__":
    print(f"合計値： {sum()}")
    print(f"最大値： {max()}")
    print(f"最小値： {min()}")
    print(f"平均値： {average()}")
