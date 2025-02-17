def fact(n):
    if n == 0:
        return 1
    else:
        fa = n * fact(n - 1)
        return fa

if __name__ == '__main__':
    print(fact(32))