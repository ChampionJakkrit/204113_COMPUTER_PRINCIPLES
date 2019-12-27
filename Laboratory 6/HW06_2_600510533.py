#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 06
# Problem 2
# 204113 Sec 02A

def main():
    list_x = [3, 7, 4, 9, 5, 2, 6, 1]
    merge_sort(list_x, show_step=True)
    print('--------')
    print(list_x)

def merge_sort(list_x, show_step=False):

    index = 0
    while index < len(list_x): # [[3],[7],[4],[9],[5],[2],[6],[1]]
        list_x[index] = [list_x[index]]
        index += 1

    list_stop = len(list_x)
    i = 0
    while list_stop >= 1: # วนหาจนเหลือ list เดียว [3,7,4,9,5,2,6,1]
        list_stop = len(list_x)
        list_stop = list_stop // 2

        if show_step == True:
            print(list_x)
            
        for l in range(i,list_stop):
            list_lx = merge_list(list_x[i], list_x[i+1]) # ส่งไปเรียงที่ละคู่
            list_x.remove(list_x[i+1]) # ลบตัวที่ 2 ก่อน เพราะ ถ้าลบตัวแรกออก จะไม่ม่ตน.ที่ 1 ให้ลบ
            list_x.remove(list_x[i])
            list_x.insert(i, list_lx) # เพิ่มเข้าไปตน.เดิม โดย i = ตน. แล้วเพิ่ม list_lx เข้าไปใน list_x เดิม
            i = i + 1
        
        i = 0 # รีเซ็ทให้ i = 0 เพื่อทำในรอบใหม่ต่อไป

    a = list_x[0]
    list_x.remove(a)
    list_x.extend(a)

def merge_list(list_a, list_b): # เอามาเทียบกัน
     len_a = len(list_a)
     len_b = len(list_b)
     i = 0
     j = 0
     list_c = []

     while i < len_a and j < len_b:
         if list_a[i] < list_b[j]:
             list_c.append(list_a[i])
             i += 1
         else:
            list_c.append(list_b[j])
            j += 1
     if i < len_a:
        list_c.extend(list_a[i:])
     if j < len_b:
        list_c.extend(list_b[j:])

     return list_c
if __name__ == '__main__':
    main()