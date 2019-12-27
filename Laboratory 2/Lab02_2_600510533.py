#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 02
# Problem 2
# 204113 Sec 02A

def main():
    print(two_complement('1101'))

def two_complement(x):
    list_x = list()
    for i in range(len(x)):
        list_x.append(1 - int(x[i])) # กลับเลข

    str_ans = ""
    carry = 1
    list_ans = [0] * len(x)
    for k in range(-1, -len(list_x) - 1, -1): # วนจากขวาไปซ้าย
        list_ans[k] = (list_x[k]) + carry # หาตัวทดเพื่อเอาไปบวกกับ list_x
        if list_ans[k] == 2:
            list_ans[k] = 0
            carry = 1 
        elif list_ans[k] == 1:
            list_ans[k] = 1
            carry = 0
        elif list_ans[k] == 0:
            carry = 0
            list_ans[k] = 0

    for s in range(len(list_ans)): # ทำ list ให้เป็น str
        str_ans += str(list_ans[s])

    return (str_ans, string_to_signed_int(str_ans))

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