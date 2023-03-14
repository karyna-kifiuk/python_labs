def squares_sum(b):
    return sum(c**2 for c in range(1, b+1))

print(squares_sum(5))
print(squares_sum(15))
print(squares_sum(16))
print(squares_sum(20))