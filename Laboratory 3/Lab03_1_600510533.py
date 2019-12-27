#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 03
# Problem 1
# 204113 Sec 02A

def main():
    i = int(input())
    print(two_power_x(i))

def two_power_x(i):
    if i & (i - 1) == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    main()
