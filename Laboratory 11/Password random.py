import random

def password_random(length):
    s = list("ABCSEFGHIJKLMNOPQRSTWUVXYZ0123456789abcdefghijklmnopqrstuvwxyz")

    return "".join(random.sample(s, length))

def replace():
    s = "password"
    r = s.replace("a", "@")
    r2 = s.replace("a", "@").replace("o", "0")
    print(r)
    print(r2)


for i in range(10):
    print(password_random(8)) 

print("-" * 40)

replace()