
unit = input("Is this temprature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temprature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"the Temprature in Fahrenheit is: {temp} °F")
elif unit == "F":
    temp = round((temp - 32) * 5 /9, 1)  
    print(f"the temprature in Celsius is: {temp} °C")
else:
    print(f"{unit} Invalid action")    
