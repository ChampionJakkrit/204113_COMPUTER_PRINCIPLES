def main():
    num = int(input())
    n = int(input())
    print(base_to_n(num, n))

def base_to_n(num, n):
    if num == 1:
        return 0
    else:
        return (num % n) + base_to_n(num // n, n) * 10

if __name__ == '__main__':
    main()