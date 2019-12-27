#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 12
# Problem 2
# 204113 Sec 02A

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))

while True:
    msg = input("-> ")

    if msg == "q":
        msg = msg.encode('ascii') # แปลงค่าจากข้อมูลไปเป็นสัญญาณ
        s.send(msg) # แล้วค่อยส่ง
        break
    
    msg = msg.encode('ascii') # แปลงค่าจากข้อมูลไปเป็นสัญญาณ
    s.send(msg) # แล้วค่อยส่ง
    msg2 = s.recv(1024) # รับค่าจาก server โดยไม่เกิน 1024

    if msg == "w":
        msg2 = "cannot calculate w"
        
    msg2 = msg2.decode('ascii') # แปลงค่าจากสัญญาณไปเป็นข้อมูล
    print("Received from server: %s" % (msg2)) # แสดงผล

s.close()

                                   


