l1 = [1,2,3,4]

print(l1.__iter__())

i = l1.__iter__()

print(i.__next__())
print(i.__next__())
print(i.__next__())
print(next(i))

s = "I love Python"
st = s.__iter__()
print(st.__next__())
print(st.__next__())
print(next(st))

for x in st:
    print(x, end="")

# Custom iterator

class Counter:
    def __init__(self, start, end):
        self.current = start - 1
        self.end = end
        print("Initializing...", self.current, self.end)

    def __iter__(self):
        return self
        print("Returning self")

    def __next__(self):
        self.current += 1
        print("Iterating")
        if self.current < self.end:
            return self.current
        else:
            print("Exception!")
            raise StopIteration

for c in Counter(3, 9):
    print(c)


cc = Counter(1,10)
print(next(cc))
print(next(cc))
print(next(cc))