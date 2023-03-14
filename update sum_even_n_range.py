def sum_even_n_range(start,stop):
    return sum(a for a in range(start, stop+1) if a % 3 == 0)

print(sum_even_n_range(69,666))
print(sum_even_n_range(9,66))
print(sum_even_n_range(6,56))
print(sum_even_n_range(96,656))