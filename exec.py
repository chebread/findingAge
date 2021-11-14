# 나이 차이 계산 프로그램

def Func(i, year):
    return year - (i - 1)

print("-- 나이 차이 계산 프로그램 --")
while True:
    choice = input("-- 생년: b / 나이: a\n(q:quit) --\n") # 나이는 Year, 생일은 Age 반환

    if choice == "q":
        print("== (QUIT) ==")
        exit()

    if choice == "b":
        age = int(input("나이: "))
        if age < 0:
            break
        if age > 2021:
            print("--생년: b.c. {}년 --".format(Func(age, 2021) * -1))
        else:
            print("--생년: {}년 --".format(Func(age, 2021)))

    elif choice == "a":
        year = int(input("생년: "))
        if year > 2021:
            break
        print("--나이: {} --".format(Func(year, 2021)))

    else:
        print("== (Error) ==")

