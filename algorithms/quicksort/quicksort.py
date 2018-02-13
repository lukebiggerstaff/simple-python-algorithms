'''
python implementation of quicksort algorithm
'''

from random import randint

def partition(list_, left, right):
    pivot = randint(left, right)
    list_[pivot], list_[left] = list_[left], list_[pivot]
    i = j = left + 1
    while j <= right:
        if list_[j] < list_[left]:
            list_[i], list_[j] = list_[j], list_[i]
            i += 1
        j += 1
    list_[left], list_[i - 1] = list_[i - 1], list_[left]
    return i - 1


def quicksort(list_, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(list_) - 1
    if right - left > 0:
        p = partition(list_, left, right)
        quicksort(list_, left, (p - 1))
        quicksort(list_, (p + 1), right)
