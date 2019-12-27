#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 09
# Problem 1
# 204113 Sec 02A

import simpy
import random

def Bank_Teller(env):

    while True:
        rand_order = random.randrange(1,3) # สุ่ม 1 กับ 2
        if rand_order == 1: # 1 = Deposit
            print('Come in %d'%env.now)
            depsit_duration = 3 # เพิ่มทีละ 3
            yield env.timeout(depsit_duration)
            print('Deposit at %d' % env.now)
            print("")
        elif rand_order == 2: # 2 = Withdraw
            print('Come in %d'%env.now)
            withdraw_duration = 5 # เพิ่มทีละ 5
            yield env.timeout(withdraw_duration)
            print('Withdraw at %d' % env.now)
            print("")
        yield env.timeout(random.randrange(1, 4))

if __name__ == '__main__':
    env = simpy.Environment()
    env.process(Bank_Teller(env))
    #start the simulation and passing an end time
    env.run(until=60)
    print("Bank close")