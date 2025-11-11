def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == to_unit:
        return value
    
    # Convert from source to Celsius first
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == 'kelvin':
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError("Invalid from_unit. Choose Celsius, Fahrenheit, or Kelvin.")
    
    # Convert from Celsius to target unit
    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return celsius_to_fahrenheit(celsius)
    elif to_unit == 'kelvin':
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError("Invalid to_unit. Choose Celsius, Fahrenheit, or Kelvin.")

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value to convert: "))
    from_unit = input("From (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    to_unit = input("To (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    
    try:
        converted = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit.capitalize()} is {converted:.2f} {to_unit.capitalize()}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
