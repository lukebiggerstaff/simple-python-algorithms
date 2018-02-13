'''
python implementation of mergesort
'''


def merge(list1, list2, sorted_list):
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            sorted_list.append(list2[j])
            j = j + 1
        else:
            sorted_list.append(list1[i])
            i = i + 1
    sorted_list += list1[i:]
    sorted_list += list2[j:]
    return sorted_list


def mergesort(list_):
    sorted_list = []
    if len(list_) == 1:
        return list_
    half = len(list_) // 2
    left = mergesort(list_[half:])
    right = mergesort(list_[:half])
    return merge(left, right, sorted_list)
