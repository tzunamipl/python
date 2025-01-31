def comp_average(number_list):
    return sum(number_list) / len(number_list)

lst = []
suma = 0

for i in range(5):
    lst.append(int(input("Provide a number: ")))
    print(lst)

print("Average value is " + str(comp_average(lst)))