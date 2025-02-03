def comp_average(number_list):
    return sum(number_list) / len(number_list)

lst = []
suma = 0

keep_asking = True

while keep_asking == True:
    user_input = input("Provide a number: ")
    if user_input != "0":
        lst.append(int(user_input))
    else:
        keep_asking = False

print(lst)
print("Average value is " + str(comp_average(lst)))