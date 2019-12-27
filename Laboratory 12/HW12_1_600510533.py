#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 12
# Problem 1
# 204113 Sec 02A

import socket                                         

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           


# establish a connection
clientsocket,addr = serversocket.accept()      
print("Connection from: %s" % str(addr))

while True:
    msg = clientsocket.recv(1024) # รับค่าจาก client โดนไม่เกิน 1024
    msg = msg.decode('ascii') # แปลงค่าจากสัญญาณไปเป็นข้อมูล

    if msg == "q":
        break # จบการทำงาน
    
    print("from connected user: %s" % str(msg))

    if msg == "w":
        msg = "cannot calculate w"
        print("cannot calculate w")
        msg = msg.encode('ascii') # แปลงข้อมูลเป็นสัญญาณแล้วส่งกลับไป
        clientsocket.send(msg)
        continue # ข้ามไป
        
    msg2 = int(msg) ** 2 # แปลงให้ยกกำลังสอง
    print("sending: %s" % str(msg2)) # แสดงผล
    msg2 = str(msg2).encode('ascii') # แปลงข้อมูลเป็นสัญญาณแล้วส่งกลับไป
    clientsocket.send(msg2)

clientsocket.close()


