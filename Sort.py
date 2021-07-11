'''
Algorithms
'''
import time
import random

'''
Bubble Sort

Runtime:
The bubble sort algorithm looks at each number in the list one at a time. Then,
it compares that number to the element one index in front. If the number in
front is smaller, they are switched. Otherwise, they stay the same. It does this
for each number in the list, and when it reaches the end, the list is sorted.
'''
def bubbleSort(listThree):
    start = time.time()
    FLAG = 0
    while FLAG == 0:
        FLAG = 1
        check = listThree
        for i in range(len(listThree)-1):
            a = listThree[i]
            b = listThree[i+1]
            if a > b:
                FLAG = 0
                listThree[i], listThree[i+1] = listThree[i+1],listThree[i]
    end = time.time()  
    return (True, [start, end], listThree)


'''
Selection Sort

Runtime:
The selection sort algorithm splits the  list into a sorted and unsorted list.
For each number(lets call this x) in the list, starting at index 0, it finds the
smallest number, and switches it with x. Then, that number is part of the
sorted list. This proccess is repeated for every number in the list, until the
list is sorted.
'''
def selectionSort(listFour):
    start = time.time()
    smallestNum = 0
    for i in range(len(listFour)):
        for x in range(i + 1, len(listFour)):
            if listFour[smallestNum] > listFour[x]:
                smallestNum = x

        listFour[i], listFour[smallestNum] = listFour[smallestNum], listFour[i]
    end = time.time()
    return (True, [start, end], listFour)


'''  
Insertion Sort

Runtime:
Insertion sort takes the second number in the list, and compares it with the
number to the left of it. If the number is smaller than the first number, then
they switch. Otherwise, they stay the same. Then, it does the same thing with
third number. If it is the smallest number out of the three, it is moved to the
beginning. If it is the second smallest, it is moved to index 1. This proccess
is repeated for every number, until the list is sorted.
'''

def insertionSort(listFive):
    start = time.time()
    for i in range(1, len(listFive)):
        key = listFive[i]
        numLess = i-1
        while numLess >=0 and key < listFive[numLess]:
            listFive[numLess+1] = listFive[numLess]
            numLess -= 1
        listFive[numLess+1] = key
    end = time.time()
    return (True, [start, end], listFive)




def mergeSort(listSix):
    if len(listSix)>1:
        mid = len(listSix)//2
        top = listSix[mid:]
        bottom = listSix[:mid]

        mergeSort(top)
        mergeSort(bottom)

        stepOne, stepTwo, stepThree = 0,0,0

        while stepOne < len(top) and stepTwo < len(bottom):
            if top[stepOne] < bottom[stepTwo]:
                listSix[stepThree] = top[stepTwo]
                stepOne+=1
            else:
                listSix[stepThree] = bottom[stepTwo]
                stepTwo+=1
            stepThree+=1

        while stepOne<len(top):
            listSix[stepThree] = top[stepOne]
            stepOne+=1
            stepThree+=1
        while stepTwo<len(bottom):
            listSix[stepThree] = bottom[stepTwo]
            stepTwo+=1
            stepThree+=1

listSix = [9, 8, 7, 5, 6, 2, 3, 4, 1, 10]
print(listSix)
mergeSort(listSix)
print(listSix)
