with open("file.txt", "r") as f:
    #print(f.read())
    for line in f:
        print(line.rstrip("\n"))

with open("new_file.txt", "a+") as f:
    f.write("Hello world!")
    f.write("\nTest 123")