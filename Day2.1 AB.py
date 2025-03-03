"""
Python program to convert the temperature in degree centigrade to Fahrenheit
"""


def celsiusToFahrenheit(cel):
    fah = (cel * 9 / 5) + 32
    return fah


celsius = float(input("Enter temperature in ℃ to convert it into ℉: "))
fahrenheit = celsiusToFahrenheit(celsius)
print(f"{celsius}℃ is equal to {fahrenheit}℉")
