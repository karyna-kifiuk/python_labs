def both(thing1, thing2):
    return (thing1<=0 and thing2 <=0) or (thing1>=0 and thing2>=0)
print(both(3,5))
print(both(-4,6))
print(both(-6,4))