def exculsive_or_dict(d1,d2):
    new_dict=dict()
    for key in d1:
        if key not in d2:
            new_dict[key]=d1[key]
    for key in d2:
        if key not in d1:
            new_dict[key]=d2[key]
    return new_dict
