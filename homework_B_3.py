x = int(input("行数を入力してください:"))
y = int(input("列数を入力してください:"))

for n in range(1, x + 1):
    for s in range(1, y + 1):

        if (s * n) < 10:
            print(end=" ")

        print("{} x {} = {}".format(s, n, s * n), end=" | ")
    print()


# for a in range(1,10):
#   for b in range(1,10):

# if (i+1)(j+1)<10:             # ← もし１桁の数なら、
#   print(end=' ')            # ← １文字分の空白を入れる

#     print('{}*{}={}'.format(a,b,a*b), end=" ")
#  print()