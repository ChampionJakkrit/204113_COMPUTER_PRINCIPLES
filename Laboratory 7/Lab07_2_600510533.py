#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 2
# 204113 Sec 02A

def main():

    p1 = [0, 2 ,3]
    p2 = [2, 4]
    print(multiply_polynomials(p1, p2))

def multiply_polynomials(p1, p2):

    idx1 = 0
    for x in range(len(p1)): # ไม่เอา 0 มาคิด
        if p1[x] != 0: # ถ้าวนเจอ 0 ให้ข้ามไป
            break
        idx1 = x + 1 # index ตัวถัดไป
    p1 = p1[idx1:len(p1)] # เอา index ตัวถัดไปถึงตัวสุดท้าย

    idx2 = 0
    for y in range(len(p2)):
        if p2[y] != 0:
            break
        idx2 = y + 1
    p2 = p2[idx2:len(p2)]

    rev_p1 = list(reversed(p1)) # กลับเพื่อจะเอาตน.จากท้าย
    rev_p2 = list(reversed(p2)) # กลับเพื่อจะเอาตน.จากท้าย

    list_ans = [0] * ((len(p1) + len(p2)) - 1) # สร้าง list คำตอบโดยจน.มากสุดคือ ดีกรีมากสุดมาบวกกัน
    for i in range(len(rev_p1)):
        for j in range(len(rev_p2)):
            list_ans[i+j] += rev_p1[i] * rev_p2[j] # ดีกรีคูณกันแล้วไปใส่ list ดีกรีนั้น
    ans = list(reversed(list_ans))

    return ans

   
if __name__ == '__main__':
    main()
    