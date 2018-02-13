'''
python binary search algorithm
'''


def binary_search(key, list_):
    first, last = 0, len(list_) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if list_[middle] == key:
            found = True
        else:
            if key < list_[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found


def recursive_binary_search(key, list_):
    if len(list_) == 0:
        return False
    else:
        middle = len(list_) // 2
        if list_[middle] == key:
            return True
        else:
            if key < list_[middle]:
                return recursive_binary_search(key, list_[middle:])
            else:
                return recursive_binary_search(key, list_[:middle])
