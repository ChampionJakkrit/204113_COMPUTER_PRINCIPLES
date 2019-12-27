#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 02
# Problem 1
# 204113 Sec 02A

def main():
    print(calculate("1101", "01000", False, 5 ))
    print(calculate("1101", "01000", True, 4 ))

def calculate(a, b, plus, length):

    max_ = max(len(a), len(b)) # หา max ของ a, b
    max_a = a[0] * (max_ - len(a)) + a # หา max ของ a โดยถ้าน้อยกว่า b ให้เติมตน.ที่ [0] ใส่ไปให้เต็ม
    max_b = b[0] * (max_ - len(b)) + b # หา max ของ b โดยถ้าน้อยกว่า a ให้เติมตน.ที่ [0] ใส่ไปให้เต็ม
    max_len = max_
    list_ans = [0] * max_len # หา list ความยาวสูงสุด 
    carry = 0
    
    if plus == False: 
        max_b = two_complement(max_b) # ทำเป็น two complement
    
    for k in range(-1, -max_len - 1, -1): # วนจากขวาไปซ้าย
        int_a = int(max_a[k])
        int_b = int(max_b[k])
    
        cal = int_a + int_b + carry
        list_ans[k] = cal % 2
        carry = cal // 2

    while carry > 0: # หาตัวเกินหลักตัวบวก 
        list_ans = [carry % 2] + list_ans
        carry //= 2

    str_ans = ""
    for s in list_ans[max_len - length + 1::]: # ทำ list ให้เป็น str โดยจำกัดความยาวหลักโดย langth
        str_ans += str(s)

    return string_to_signed_int(str_ans)

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

    return (str_ans)
if __name__ == '__main__':
    main()
