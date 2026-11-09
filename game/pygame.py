celsius = float(input("Zadej teplotu ve stupnich Celsia: "))

fahrenheir = round(celsius * 9 / 5 + 32, 2) #Prevod z celsia do fahrenheitu
kelvin = round(celsius + 273.15, 2)

print(f"{celsius} °C = {fahrenheir} °F = {kelvin} K")
