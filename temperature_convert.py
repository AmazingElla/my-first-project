def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def convert_temperature(value, from_unit, to_unit):
    if not isinstance(from_unit, str):
        raise ValueError("Invalid unit")
    if not isinstance(to_unit, str):
        raise ValueError("Invalid unit")
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError("Invalid temperature")

    if from_unit not in ("celsius", "fahrenheit", "kelvin"):
        raise ValueError("Invalid unit")
    if to_unit not in ("celsius", "fahrenheit", "kelvin"):
        raise ValueError("Invalid unit")
    if from_unit == "celsius" and value < -273.15:
        raise ValueError("Temperature below absolute zero")

    if from_unit == "fahrenheit" and value < -459.67:
        raise ValueError("Temperature below absolute zero")

    if from_unit == "kelvin" and value < 0:
        raise ValueError("Temperature below absolute zero")

    if from_unit == to_unit:
        return value
    
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return celsius_to_fahrenheit(value)
    
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return fahrenheit_to_celsius(value)
    
    elif from_unit == "celsius" and to_unit == "kelvin":
        return celsius_to_kelvin(value)
    
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return celsius_to_kelvin(fahrenheit_to_celsius(value))
    
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return celsius_to_fahrenheit(value - 273.15)