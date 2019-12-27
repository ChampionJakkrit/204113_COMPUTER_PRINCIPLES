#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 08
# Problem 1
# 204113 Sec 02A

from random import randint

def rand_sym():

    print("Lock = 0")
    print("Paper = 1")
    print("Scissor = 2")
    print("")

    human_win = 0
    comp_win = 0
    for i in range(3): # วนสุ่ม 3 รอบ
        n = int(input("You: "))
        r = randint(0, 2) # สุ่มเลข 0- 2
        if n == 1 and r == 0:
            human_win += 1
            print("Computer: 0")
        elif n == 0 and r == 2:
            human_win += 1
            print("Computer: 2")
        elif n == 2 and r == 1:
            human_win += 1
            print("Computer: 1")

        if r == 1 and n == 0:
            comp_win += 1
            print("Computer: 1")
        elif r == 0 and n == 2:
            comp_win += 1
            print("Computer: 0")
        elif r == 2 and n == 1:
            comp_win += 1
            print("Computer: 2")

        elif n == 0 and r == 0: # กรณีเสมอกัน
            print("Computer: 0")
        elif n == 1 and r == 1:
            print("Computer: 1")
        elif n == 2 and r == 2:
            print("Computer: 2")

    print("")
    if human_win > comp_win: # ถ้าคนชนะเยอะว่าคอม
        print("You Win!!")
    elif comp_win > human_win: # ถ้าคอมชนะเยอะว่าคน
        print("Computer Win!!")
    elif human_win == comp_win: # ถ้าเสมอกัน
        print("Draw")


if __name__ == '__main__':
    rand_sym()
    