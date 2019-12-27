#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 13
# Problem 1
# 204113 Sec 02A

import random
import threading

response = None

def main():
    count_score = 0
    for i in range(1, 11):
        score = play_question()
        if score == 1:
            count_score += 1
        if score == "q":
            break
    print("You've got: %d"%count_score)
    print("bye!!")

def generate_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = ("{:2} + {:2} = ".format(a,b))
    result = str(a + b)

    return question, result

def user_input():
    global response
    response = input()
    question, result = generate_question()
    

def play_question():
    global response
    response = None # เชตให้เป็น 0 ก่อน input ก่อนตลอด
    user = threading.Thread(target=user_input)
    question, result = generate_question()
    print(question, end="")
    user.daemon = True
    user.start()
    user.join(5)

    if response != result and response != None and response != "q" and response != "Q":
        print("Try again")
    if response == result:
        print("Correct!!")
        return 1
    if response is None:
        print('Timeout!!')
        return 0
    if response == "q" or response == "Q":
        return "q"

if __name__ == '__main__':
    main()






