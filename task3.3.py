lst = []
suma = 0
num = 6

while num != "0":
    num = input("Provide a number: ")
    lst = lst + list(num)
    suma += int(num)
    print(lst)
    print(suma)

print("Average value is " + str(suma / len(lst)))