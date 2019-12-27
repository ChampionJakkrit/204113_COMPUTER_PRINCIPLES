def main():
    init_money = float(input("Enter initial money:"))
    in_rate = float(input("Interest rate:"))
    period = int(input("Enter year period:"))
    print("The toal money is",end = " ")
    print("%.2f"%(deposit_cal(init_money,in_rate,period)))

def deposit_cal(init_money, in_rate, period):
    if period == 0:
        return init_money
    else:
        return deposit_cal(init_money + init_money * in_rate // 100, in_rate, period - 1)

if __name__ == '__main__':
    main()