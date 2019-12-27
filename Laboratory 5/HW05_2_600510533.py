#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 05
# Problem 2
# 204113 Sec 02

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
        print()


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

    def count(self): # สร้าง method มานับ
        currnode = self.root
        count = 0
        while currnode != None:
            count = count + 1
            currnode = currnode.get_next()
        return count


#------------------end of class LinkedList -------------------#

def vowelCount(word):
    index_a = LinkedList() # สร้าง list ว่างขึ้นมาใส่สระแต่ละตัว
    index_e = LinkedList()
    index_i = LinkedList()
    index_o = LinkedList()
    index_u = LinkedList()
    for ch in word: # หาตัว a e i o u เพิ่มใน list ว่างๆที่สร้างมา

        if ch == "a":
            index_a.add("a")

        if ch == "e":
            index_e.add("e")

        if ch == "i":
            index_i.add("i")

        if ch == "o":
            index_o.add("o")

        if ch == "u":
            index_u.add("u")

    print("{} {} {} {} {}".format(index_a.count(), index_e.count(), index_i.count(), index_o.count(), index_u.count()))
            
def main():
    # word = LinkedList()
    word1 = "happy birthday"
    wordlower = word1.lower()
    vowelCount(wordlower)

    word2 = "Recursive function"
    wordlower = word2.lower()
    vowelCount(wordlower)

    word3 = "puzzle games"
    wordlower = word3.lower()
    vowelCount(wordlower)

    word4 = "Fight for my mom"
    wordlower = word4.lower()
    vowelCount(wordlower)

    word5 = "Jakkrit Boonnet"
    wordlower = word5.lower()
    vowelCount(wordlower)

    word6 = "Theconquerorz"
    wordlower = word6.lower()
    vowelCount(wordlower)

    word7 = "Preawthida Luangchai"
    wordlower = word7.lower()
    vowelCount(wordlower)

    word8 = "Kukkik"
    wordlower = word8.lower()
    vowelCount(wordlower)

    word9 = "Champion"
    wordlower = word9.lower()
    vowelCount(wordlower)

    word10 = "Kadsarin Sanjum"
    wordlower = word10.lower()
    vowelCount(wordlower)

    word11 = "Fight for the future"
    wordlower = word11.lower()
    vowelCount(wordlower)
    
if __name__ == '__main__':
    main()

    # funtion = funtion(paramiter) [อยู่นอก class]
    # method = paramiter.method()  [อยู่ใน class]