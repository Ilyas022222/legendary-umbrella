def convert_temperature():
    conversion_type = input("Type 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").strip().upper()
    temperature = float(input("Enter the temperature you want to convert: "))
    if conversion_type == 'C':
        converted_temp = (temperature * 9/5) + 32
       print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
       elif conversion_type == 'F':
       converted_temp = (temperature - 32) * 5/9
       print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
   else:
       print("Please type 'C' or 'F'.")
