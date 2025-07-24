def has_duplicate(MyList):
    set_list = set(MyList)
    return len(set_list) != len(MyList)