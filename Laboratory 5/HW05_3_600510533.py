#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 05
# Problem 3
# 204113 Sec 02A

def prime_factorize(x): # หาจำนวนเฉพาะ
    return [1] + prime(x, 2)

def prime(x,c):
    if c * c > x:
        return [x]

    if x % c == 0:
        return [c] + prime(x // c, c)
    else:
        return prime(x, c + 1)

def main():
    print(prime_factorize(4))
    print(prime_factorize(180))
    print(prime_factorize(10))



if __name__ == '__main__':
    main()
