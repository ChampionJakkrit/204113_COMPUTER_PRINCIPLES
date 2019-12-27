#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 03
# Problem 1
# 204113 Sec 02A

def main():
    print(IP_encode("1", "10.28.4.2"))
    print(IP_encode("2", "3232237069"))

def IP_encode(mode, text):
    if mode == "1":
        list_n = [] # ทำให้เป็น int
        n = text.split(".")
        for i in range(len(n)):
            list_n.append(int(n[i]))
        shitf = [24, 16, 8, 0]
        ans = 0
        for x in range(4):
            ans += list_n[x] << shitf[x]
        return str(ans)

    else:
        bin_t = bin(int(text)) # เปลี่ยนเป็นฐาน 2
        list_2 = []
        x = 2
        y = 10
        for i in range(4): # [x,x,x,x] สร้างคำตอบ 4 หลัก
            list_2.append(str(bin_t[x:y])) # ใส่ 8 bit เข้าไปในลิสหลักที่ 1,2,3,4 
            x = y
            y += 8
        ans = ""
        c = 0
        for i in list_2: # ทำฐาน 2 ให้เป็นฐาน 10
            ans += str(int(i, 2))
            c += 1
            if c != len(list_2): # ใส่จุดคั่น
                ans += "."
        return ans

if __name__ == '__main__':
    main()

