def main():
    a = int(input())
    n = int(input())
    d = int(input())
    print(sum(a, n, d))

def sum(a, n, d):
    if n == 1:
        return a
    else:
        return a + sum(a + d, n - 1, d)

if __name__ == '__main__':
    main()