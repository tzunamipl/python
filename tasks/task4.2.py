city_list = []

with open("tasks/cities", "r") as f:
    for line in f:
        city_list.append(line.rstrip("\n"))

sorted_city_list = sorted(city_list)

print(sorted_city_list)
with open("ordered_cities", "w") as f:
    for city in sorted_city_list:
        f.write(city + "\n")

print("Done!")