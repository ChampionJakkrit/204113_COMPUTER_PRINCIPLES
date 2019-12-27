#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 08
# Problem 2
# 204113 Sec 02A

import time
import datetime

def qrand_dice():

    ra1 = random_quadratic(1)
    print("Computer A: %d"%ra1)
    comp_a1 = abs(ra1 - 8) # เลขระยะห่างของ com_a ใกล้เลข 8 รอบ1

    rb1 = random_quadratic(2)
    print("Computer B: %d"%rb1)
    comp_b1 = abs(rb1 - 8) # เลขระยะห่างของ com_b ใกล้เลข 8 รอบ1

    ra2 = random_quadratic(3)
    print("Computer A: %d"%ra2)
    comp_a2 = abs(ra2 - 8) # เลขระยะห่างของ com_a ใกล้เลข 8 รอบ2

    rb2 = random_quadratic(4)
    print("Computer B: %d"%rb2)
    comp_b2 = abs(rb2 - 8) # เลขระยะห่างของ com_a ใกล้เลข 8 รอบ2

    print("")

    if comp_a1 + comp_a2 < comp_b1 + comp_b2: # ถ้าเลขระยะห่าง com_a < เลขระยะห่าง com_b
        print("Computer A Win!!") 

    elif comp_b1 + comp_b2 < comp_a1 + comp_a2: # ถ้าเลขระยะห่าง com_b < เลขระยะห่าง com_a
        print("Computer B Win!!")

    elif comp_b1 + comp_b2 == comp_a1 + comp_a2: # ถ้าเลขระยะห่าง com_a == เลขระยะห่าง com_b
        print("Draw")

def random_quadratic(x):

    d = datetime.datetime.now()
    m = d.microsecond
    a = d.minute
    b = d.second
    c = d.second
    xn = time.time()
    
    xn = (a * xn ** 2 + b * xn + c) % m
    xn = xn + x
    xn = xn % 7 # จำกัดขอบเขต 0- 6
    if xn == 0: # ถ้าสุ่มได้เลข 0 ให้ บวกขึ้น 1
        xn = xn + 1
    xn = int(xn) # ทำให้เป็นจำนวนเต็ม
    return xn

if __name__ == '__main__':
    qrand_dice()