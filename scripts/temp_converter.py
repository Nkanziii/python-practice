temperature_val = float(input("Enter temperature: ")) 
temp_degrees = input("Is it C or F? ")


# if user said Celsius convert to ferenheit and return the result 
if temp_degrees == "C":
    celsius_value = (temperature_val * 9/5) + 32
    print(f"{temperature_val} {temp_degrees} = {celsius_value}" )
elif temp_degrees == "F":
    Fahrenheit_value = (temperature_val - 32) * 5/9
    print(f"{temperature_val} {temp_degrees} = {Fahrenheit_value}")
else:
    print("Invalid Input")
