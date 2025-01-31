user_age = input("How old are you? ")
month = "July"

if int(user_age) >= 25:
    print("You're officaially an adult")
elif int(user_age) >= 18:
    print("You are young adult")
else:
    print("You're not adult yet")

if month in ["June","July","August"]:
    print("It's summer!")

print("End of orogram")