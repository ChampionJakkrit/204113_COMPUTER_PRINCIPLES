#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 04
# Problem 2
# 204113 Sec 02A


# definition of node containing data and pointer to next node
class Node(object):

    # constructor
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

# getter and setter method
    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

#------------------end of class Node -------------------#

# Definition of class LinkedList containing root node location


class LinkedList(object):

    def __init__(self, r=None):
        self.root = r

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node

    # traverse along the list and print value of each node, seperate the
    # value with " "
    def print(self):

        currnode = self.root

        while currnode:
            print(currnode.get_data(), end=" ")
            currnode = currnode.get_next()
        print()

    # insert value d in the linked list with ascending order

    def append(self, d):
        newnode = Node(d, None) # สร้าง newnode

        if self.root == None:
            self.add(d)

        else:
            currnode = self.root # ตัวแรก
            while currnode.get_next() != None:
                currnode = currnode.get_next() # วนไปจนกว่าจะเจอตัวสุดท้าย ซึ่ง currnode จะเป็นตัวรองสุดท้าย
            currnode.set_next(newnode) # ให้ currnode (ตัวสุดท้าย) ชี้ newnode(จะต่อหลัง)

    def rprint(self):

        currnode = self.root
        list_curr = [] # สร้าง list
        while currnode: # นับแต่ละตัวทั้งหมด
            d = currnode.get_data()
            list_curr.append(d) # ใส่ data ทีละตัวใน list
            currnode = currnode.get_next() # ให้ currnode ชี้ตัวถัดไปเรื่อยๆ
        re_list = reversed(list_curr) # กลับเลขใน list
        for i in re_list: # วนทีละตัวใน list ที่กลับ
            print(i, end = " ")

def main():

    myList = LinkedList()

    order = input().split(" ")
    order = list(map(int, order))
    for item in order:
        myList.append(item)

    myList.print()
    myList.rprint()


if __name__ == '__main__':
    main()
