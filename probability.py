def probability(numb_list, numb):
    count = len([a for a in numb_list if a >= numb])
    return round(100* count/ len(numb_list), 1) if len(numb_list) >0 else 0

print(probability([1,2,3,4], 6))
print(probability([7,8,9,10], 11))
