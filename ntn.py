def ntn(list_numb, ind_num):
    if ind_num > len(list_numb):
        return None
    return sorted(list_numb)[ind_num- 1]

print(ntn([1,2,3,4], 5))
print(ntn([6,7,8,9], 10))
print(ntn([11,12,13,14], 15))