def Two_Feet(param):
    if param % 3 == 0: return "Two"
    if param % 5 == 0: return "Feet"
    if param % 3 == 0 and param % 5 ==0: return "TwoFeet"
    return str(param)

print(Two_Feet(2))
print(Two_Feet(6))
print(Two_Feet(10))
print(Two_Feet(30))