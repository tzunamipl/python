def generator_demo():
    i = 1
    print("First")
    yield i

    i += 1
    print("Second")
    yield i

gen = generator_demo()
print(gen.__next__())
print(gen.__next__())

print("Another generator")

def generator_next():
    for i in range(10):
        yield i

gennext = generator_next()
for n in range(10):
    print(gennext.__next__(), end="-")
print("")