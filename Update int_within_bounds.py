def int_within_bounds (thing, two_bound, feet_bound):
    if type(thing) !=int:
        return False
    elif thing >= two_bound and thing < feet_bound:
            return True
    else:
            return False

    print(int_within_bounds(1,2,3))
    print(int_within_bounds(4,5,6))
    print(int_within_bounds(7,8,9,10))