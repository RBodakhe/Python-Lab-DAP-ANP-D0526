"""
Python program to convert the temperature in degree centigrade to Fahrenheit 
"""
def fahrenheitToCelsius(fah):
    cel = (fah - 32) * 5 / 9
    return cel


fahrenheit = float(input("Enter temperature in ℉ to convert it into ℃: "))
celsius = fahrenheitToCelsius(fahrenheit)
print(f"{fahrenheit}℉ is equal to {celsius}℃ ")
