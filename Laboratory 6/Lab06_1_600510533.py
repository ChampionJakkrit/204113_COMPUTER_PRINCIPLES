#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 06
# Problem 1
# 204113 Sec 02A

def main():
    list_x = ["11/1/2100", "5/12/1999", "19/1/2003", "11/9/2001"]
    sort_date(list_x, show_step=True)
    print("---")
    print(list_x)

def sort_date(list_x, show_step=False):

    for i in range(1, len(list_x), 1): # i = ตน.ที่เพิ่มไปเรื่อยๆทีละ 1
        j = i # j คือตน.ที่ลดลงเรื่อยๆทีละ 1
        while j >= 1 and less_than(list_x[j], list_x[j - 1]): # ถ้าตัวลองสุดท้าย > ตัวสุดท้าย ให้สลับ
            list_x[j], list_x[j - 1] = list_x[j - 1], list_x[j] # สลับ
            j = j - 1
        if show_step == True:
            print("%d:"%i,end = " ") #1:, 2:, 3:
            print(list_x)

def less_than(date1, date2):

    list_a = list(map(int, date1.split("/"))) # [xx, x, xxxx]
    list_b = list(map(int, date2.split("/")))

    for i in range(2, -1, -1): # วนจากปีไปเดือนไปวัน
        if list_a[i] < list_b[i]:
            return True
        elif list_a[i] > list_b[i]:
            return False
        else:
            pass # ถ้า มันจะเลื่นไปเดือนไปวันเอง

if __name__ == '__main__':
    main()