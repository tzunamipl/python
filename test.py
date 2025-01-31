print("Hello test")

def ctof(temp):
    return float(temp) * 1.8 + 32

temp = input("What is current temperature in Celcius? ")

print("Temperature " + str(temp) + "C is " + str(ctof(temp)) + "F")