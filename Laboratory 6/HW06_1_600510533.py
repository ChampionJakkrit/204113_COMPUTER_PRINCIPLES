#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 06
# Problem 1
# 204113 Sec 02A

def main():
    list_x = [19, 48, 175, 290, 873, 7, 43, 69]
    radix_int(list_x, show_step=True)
    print('--------')
    print(list_x)


def radix_int(list_x, show_step=False):
    max_ = 0
    for i in range(len(list_x)): # หาหลักที่มากที่สุด
        num = count_digits(list_x[i])
        if num > max_:
            max_ = num

    list_box = [[], [], [], [], [], [], [], [], [], []]
    for i in range(-1, -max_ - 1, -1): # วนตามหลักที่มากที่สุดใน list_x
        n = len(list_x)
        for j in range(n):
            get_pop = list_x.pop(0) # เก็บค่าที่ pop ออกมา
            persent = int(str("0" * (max_ - len(str(get_pop))) + str(get_pop))[i]) 
            list_box[persent].append(get_pop) # เอาออกมาเรียงใหม่
        for j in range(10):
            m = len(list_box[j])
            for k in range(m):
                list_x.append(list_box[j].pop(0))

        if show_step == True:
            print(list_x)

def count_digits(num): # นับจำนวนหลัก

    count = 0
    while num != 0:
        present = num // 10
        count = count + 1
        num = present
    return count


if __name__ == '__main__':
    main()


