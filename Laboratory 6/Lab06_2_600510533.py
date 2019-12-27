#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 06
# Problem 2
# 204113 Sec 02A

def main():
    list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),
              ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
              ("9/3/2013", "Event E"), ("11/3/2017", "Event F"),
              ("7/5/2019", "Event G"), ("29/2/2032", "Event H"),
              ("9/11/2042", "Event I")]
    event = search_event(list_x, "23/8/2008", show_step=True)
    print("---")
    print(event)

def search_event(list_x, key, show_step=False):
    
    lo = 0 # ขแบล่าง
    hi = len(list_x) - 1 # ขอบบน
    while lo <= hi: # วนหาตรงกลาง
        mid = (lo + hi) // 2
        if less_than(key, list_x[mid][0]): #  ถ้าตัวที่จะหา < ตรงกลาง ("29/02/2032") < [9/11/2042] (= ตน.ที่ 0 = "9/11/2042")
            hi = mid - 1 # ขยับขอบบนมาแทนตน. mid
        elif less_than(list_x[mid][0], key): # ตัวที่จะหา > ตรงกลาง
            lo = mid + 1 # ขยับขอบล่างมาแทนตน. mid
        else:
            return str(list_x[mid][0]), str(list_x[mid][1]) # ถ้าเจอแล้ว คืนค่า ตน.ที่0 กับ ตน.ที่1 ("9/11/2042", "Event I")

        if show_step == True:
            # for i in range(len(list_x[mid])):
            print("[%d]:"%mid, end = " ")
            print(str(list_x[mid][0]))

    return None # ถ้าไม่เจอคืนค่า None

def less_than(date1, date2):

    list_a = list(map(int, date1.split("/"))) # [9,11,2042]
    list_b = list(map(int, date2.split("/")))

    for i in range(2, -1, -1): # วนจากปีไปเดือนไปวัน
        if list_a[i] < list_b[i]:
            return True
        elif list_a[i] > list_b[i]:
            return False
        else:
            pass # ถ้าเท่ากัน มันจะเลื่นไปเดือนไปวันเอง

    return False # กรณีเท่ากัน


if __name__ == '__main__':
    main()