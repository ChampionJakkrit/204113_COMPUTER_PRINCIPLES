#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 08
# Problem 1
# 204113 Sec 02A

import time
import datetime
from pylab import *

def main():

    rand_float(300)

def rand_float(x):

    d = datetime.datetime.now()
    m = d.microsecond
    a = d.minute
    c = d.second
    xn = time.time()

    lsit_x = []
    lsit_y = []
    for i in range(x):
        lsit_y.append(i)
        xn = (a*xn + c) % m

        while xn > 1: # หาช่วง แกน y ระหว่าง 0- 1
            xn = (x / xn) % 1
        lsit_x.append(xn)

    plot(lsit_y,lsit_x, ls=' ', marker='.')
    show()

if __name__ == '__main__':
    main()