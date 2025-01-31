lst = []
suma = 0

for i in range(5):
    num = input("Provide a number: ")
    lst = lst + list(num)
    suma += int(num)
    print(lst)
    print(suma)

print("Average value is " + str(suma / len(lst)))