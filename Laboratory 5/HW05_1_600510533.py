#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 05
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
        while currnode:  # วนแค่ data ทั้งหมด
            if currnode.get_data() == d:  # ถ้าข้อมูลเหมือนตัวที่จะลบ
                if prev:  # ตัวก่อนหน้า currnode จะไม่ใช่ none
                    # ชี้ไปตัวที่จะลบก่อน แล้วค่อยชี้ไปตัวถัดไปอีกที
                    prev.set_next(currnode.get_next())
                    count += 1
                else:  # ถ้าไม่ใช่ชี้ตัวถัดไป
                    self.root = currnode.get_next()
            prev = currnode
            currnode = currnode.get_next()

        if count != 0:  # ถ้าโดนลบ
            return True
        else:
            return False

    # traverse along the list and print value of each node, seperate the
    # value with " "

    def print(self):
        currnode = self.root
        while currnode:  # วนแค่ข้อมูลตัวมันเอง
            print(currnode.get_data(), end=" ")
            currnode = currnode.get_next()

    # insert value d in the linked list with ascending order
    def insert_in_order(self, d):

        if self.root == None or self.root.get_data() >= d:
            return self.add(d)
        else:
            currnode = self.root
            while currnode.get_next() != None and currnode.get_next().get_data() < d:
                # ให้ cur เท่ากับตัวถัดไปเพื่อเปรียบเทียบ
                currnode = currnode.get_next()

            newnode = Node(d, None)  # สร้าง newnode
            # next ของ new ไปชี้cur.getnext (new_node.get_next = curr.get_next)
            newnode.set_next(currnode.get_next())
            currnode.set_next(newnode)  # cur ไปชี้ที่ d ใหม่

        return newnode


#------------------end of class LinkedList -------------------#

def linear_search(key, l):
    index = 0
    cur = l.root
    while cur != None: # วนหาทั้งหมด
        if key == cur.get_data(): # ถ้าเช็คเจอให้รีเทิร์น ตำแหน่งนั้นออกไป
            return index
        cur = cur.get_next() # วนไปเรื่อยๆ
        index = index + 1

    if cur == None: # ถ้าไม่เจอให้รีเทิร์น None
        return None
    else:
        return index


def main():
    mylist = LinkedList()
    mylist.insert_in_order(8)
    mylist.insert_in_order(6)
    mylist.insert_in_order(9)
    mylist.insert_in_order(1)
    mylist.insert_in_order(2)
    mylist.insert_in_order(5)
    mylist.insert_in_order(10)
    mylist.insert_in_order(4)
    mylist.insert_in_order(3)
    mylist.insert_in_order(7)
    mylist.insert_in_order(11)
    mylist.insert_in_order(12)


    assert(linear_search(1, mylist) == 0)
    assert(linear_search(2, mylist) == 1)
    assert(linear_search(3, mylist) == 2)
    assert(linear_search(4, mylist) == 3)
    assert(linear_search(5, mylist) == 4)
    assert(linear_search(6, mylist) == 5)
    assert(linear_search(7, mylist) == 6)
    assert(linear_search(8, mylist) == 7)
    assert(linear_search(9, mylist) == 8)
    assert(linear_search(10, mylist) == 9)
    assert(linear_search(12, mylist) == 11)


if __name__ == '__main__':
    main()
