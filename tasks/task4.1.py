from classes.module import list_average

number_list = []

with open("numbers", "r") as f:
    for line in f:
        number_list.append(float(line.rstrip("\n")))

print(number_list)
print(list_average(number_list))