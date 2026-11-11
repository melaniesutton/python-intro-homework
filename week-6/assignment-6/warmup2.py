def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Celsius to Fahrenheit
print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"43°C = {celsius_to_fahrenheit(43):.1f}°F")
print(f"67°C = {celsius_to_fahrenheit(67):.1f}°F")

# Fahrenheit to Celsius
print(f"0°F = {fahrenheit_to_celsius(0):.1f}°C")
print(f"75°F = {fahrenheit_to_celsius(75):.1f}°C")
print(f"23°F = {fahrenheit_to_celsius(23):.1f}°C")