def calculate_fuel(distance):
    fuel= distance *10
    if fuel<100:
        fuel = 100
    return fuel
print(calculate_fuel(30))
print(calculate_fuel(80))
print(calculate_fuel(270))
