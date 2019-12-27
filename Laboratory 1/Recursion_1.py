def main():
    a = int(input())
    n = int(input())
    print(pow(a, n))

def pow(a, n):
    if n == 1:
        return a
    else:
        return a * pow(a, n-1)

if __name__ == '__main__':
    main()
