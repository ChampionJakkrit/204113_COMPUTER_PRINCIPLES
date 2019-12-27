#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 1
# 204113 Sec 02A

def main():

    word = input()
    print(permute(word))

def permute(word):

    list_word = list(word)
    list_result = [list_word.pop()] # เอาตัวหลังออก

    while len(list_word) != 0:
        letter = list_word.pop() # เอาตัวหลังตัวที่สองออก
        list_ans = []
        for i in list_result:
            for j in range(len(i) + 1):
                list_ans.append(i[:j] + letter + i[j:])
        list_result = list_ans
    
    return list(set(list_result)) # เอาตัวซ้ำออก

if __name__ == '__main__':
    main()