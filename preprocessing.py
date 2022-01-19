def list_compare(list1: list, list2: list):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    for a,b in zip(list1, list2):
        if a != b:
            return False
            
    return True