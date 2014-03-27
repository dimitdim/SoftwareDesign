import types
def recursive_flatten(list):
    new=[]
    for item in list:
        if type(item)==types.ListType:
            sub=recursive_flatten(item)
            for sitem in sub:
                new.append(sitem)
        else:
            new.append(item)
    return new
