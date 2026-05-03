def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(mi):
    return mi / 0.621371

while True:
    print("\nUnit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Quit")

    choice = input("Pick 1-5: ")

    if choice == "1":
        value = float(input("Enter Celsius: "))
        print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
    elif choice == "2":
        value = float(input("Enter Fahrenheit: "))
        print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
    elif choice == "3":
        value = float(input("Enter kilometers: "))
        print(f"{value} km = {km_to_miles(value):.2f} miles")
    elif choice == "4":
        value = float(input("Enter miles: "))
        print(f"{value} miles = {miles_to_km(value):.2f} km")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")