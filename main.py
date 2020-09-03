temp = input("Enter temperature: ")
temp = float(temp)
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  print(f"Converting Fahrenheit to Celcius.")
  Celsius = float(temp)
  Celsius = (temp * 9/5) + 32
  print({str(temp)} + "% in Fahrenheit is equivalent to" + {str(Celsius)} + "% Celcius."
elif unit == "C" or unit == "c":
  print(f"Converting Celcius to Farenheit")
  Fahrenheit = float(temp)
  Fahrenheit = (temp - 32) * 5/9
  print({str(temp)} + "% in Celsius is equivalent to" + {str(Fahrenheit)} + "% Fahrenheit."
else:
  print("fInvalid unit()")

