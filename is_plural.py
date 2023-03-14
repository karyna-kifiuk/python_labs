def is_plural(word):
    if word.endswith("s"):
        return True
    else:
        return False

print(is_plural("two"))
print(is_plural("feet"))
print(is_plural("her"))
print(is_plural("life"))