a = 10
print(a)

def outer():
    a = 15
    print("Outer:", a, id(a))

def inner():
    global a
    b = 20
    print("Inner", b, id(b))
    a = 12

if __name__ == '__main__':
    outer()
    print(a)
    inner()
    print(a)