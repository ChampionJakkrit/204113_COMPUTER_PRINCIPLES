#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 02
# Problem 1
# 204113 Sec 02A

def main():
    print(string_to_signed_int('1101'))

def string_to_signed_int(x):

    list_x = list()
    for i in x:
        list_x += i

    sum_ = 0
    for i in range(len(list_x)):
        if i == 0:
            sum_ -= int(list_x[i]) * (2 ** (len(list_x) - 1)) # ตัวหลักแรก ให้คูณ -1 เข้าไป
        else:
            sum_ += int(list_x[i]) * (2 ** (len(list_x) - i - 1)) # ผลรวมหลักที่สองเป็นต้นไป (2 กำลังหลัก-1)

    return sum_

if __name__ == '__main__':
    main()