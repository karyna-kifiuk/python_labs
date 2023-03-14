def filter_list(list_with_str_int):
    return [a for a in list_with_str_int if isinstance(a, int)]

print(filter_list([1,2,3,4]))
print (filter_list(["Two", "Feet"]))
