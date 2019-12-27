#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 04
# Problem 1
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

    # remove node with value d from the linkedlist, return True if data is
    # removed, return False if not found
    
    def remove(self, d):
        prev = None
        currnode = self.root
        count = 0
        while currnode: # วนแค่ data ทั้งหมด
            if currnode.get_data() == d: # ถ้าข้อมูลเหมือนตัวที่จะลบ
                if prev: # ตัวก่อนหน้า currnode จะไม่ใช่ none
                    prev.set_next(currnode.get_next()) # ชี้ไปตัวที่จะลบก่อน แล้วค่อยชี้ไปตัวถัดไปอีกที
                    count += 1
                else: # ถ้าไม่ใช่ชี้ตัวถัดไป
                    self.root = currnode.get_next()
            prev = currnode
            currnode = currnode.get_next()
            
        if count != 0: # ถ้าโดนลบ
            return True
        else:
            return False

        

    # traverse along the list and print value of each node, seperate the
    # value with " "

    def print(self):
        currnode = self.root
        while currnode: # วนแค่ข้อมูลตัวมันเอง
            print(currnode.get_data(),end = " ")
            currnode = currnode.get_next() 


    # insert value d in the linked list with ascending order
    def insert_in_order(self, d):

        if self.root == None or self.root.get_data() >= d:
            return self.add(d)
        else:
            currnode = self.root
            while currnode.get_next() != None and currnode.get_next().get_data() < d:
                currnode = currnode.get_next() # ให้ cur เท่ากับตัวถัดไปเพื่อเปรียบเทียบ

            newnode = Node(d, None) # สร้าง newnode
            newnode.set_next(currnode.get_next()) # next ของ new ไปชี้cur.getnext (new_node.get_next = curr.get_next)
            currnode.set_next(newnode) # cur ไปชี้ที่ d ใหม่

        return newnode

#------------------end of class LinkedList -------------------#



def main():  # *****DO NOT EDIT *****

    # process each line of input as follow mode:
    # i: insert value in the list in ascending order
    # d: delete node with specific order
    #       print "value [removed]" if the command success
    #       print "value [not removed]" if the command fail
    # t: traverse and print the list with calling myList.traverse()

    myList = LinkedList()

    total = int(input())
    for i in range(total):
        order = input().split(" ")

        if order[0] == 'i':
            myList.insert_in_order(int(order[1]))
        elif order[0] == 'd':
            i = int(order[1])
            result = myList.remove(i)
            if result:
                print(i, "[removed]")
            else:
                print(i, "[not removed]")
        elif order[0] == 'p':
            myList.print()


if __name__ == '__main__':
    main()
