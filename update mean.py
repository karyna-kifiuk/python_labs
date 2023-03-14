def mean(thing):
    digits = [int(a) for a in str(thing)]
    return sum(digits) //  len(digits)

print(mean(27))
print(mean(72))
print(mean(9))