import time
import random
'''
Linear Search

Runtime:
Linear search takes every number in the list, and checks if it is equal to the
entered number. It repeats this until the number is found in the list.

'''


def linearSearch(t, l):
    start = time.time()
    for num in l:
        if num == t:
            end = time.time()
            return (True, [start, end], l.index(num))
    return None


'''
Bianary Search

Runtime:
Binary search takes the list,which it assumes is sorted ,and finds the mid
point. If the number at the mid point is equal to the entered number,
then it returns that number. If the mid point is greater than the entered
number, it repeats the proccess again, but with the bottom half of the list. If
the mid point is smaller than the entered number, than  it repeats the proccess
with the top half of the list. This is repeted until the number is found.
'''
def binarySearch(listTwo,x, high, low):

    start = time.time()
    if high>=low:
        mid = (high + low)//2
        if listTwo[mid] == x:
            end = time.time()
            return (True, [start, end], mid)
        elif listTwo[mid] > x:
            return binarySearch(listTwo, x, mid-1, low)
        elif listTwo[mid] < x:
            return binarySearch(listTwo, x, high, mid+1)
    else:
        return None
