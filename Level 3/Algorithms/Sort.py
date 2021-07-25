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

This sorting algorithm is really simple, so its good for short lists, but it
takes the longest out of the sorting algorithms on longer lists.
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

Like the bubble sort, this algrotihm is quite simple, so it does well on shorter
lists, but, unlike the bubble sort ,it also does average on longer lists. 
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

Insertion sort is a bit more complicated than the selection and bubble sort, but
it is the fastest on the mid length lists, and is really fast on shorter lists
as well.
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


'''
Merge Sort
Runtime:
The merge sort algorithm takes in a list as a parameter. Making sure that the
list length is greater than 1, first, it finds the mid point of the list, and
splits it into two lists, the left half, and the right half. Then, it calls
itself with both of those halves. This is going to create a recursive loop.
Then, it merges those sorted halves in a way that they stay sorted. Basically,
for every index in each half of the list, it check which one is smaller. Then, it
adds that number to the list, and adds one to that sides index. It repeats this
proccess till it has iterated through the list. Then, it adds the leftover
numbers.

The merge sort is the most complex sorting algorithm out of the four, and does
the best on the longest lists, and beats insertion sort by over a minute with a
30, 000 element list. 
'''

def mergeSort(listSix):
    start = time.time()
    if len(listSix) > 1:
        mid = len(listSix)//2
        left = listSix[:mid]
        right = listSix[mid:]

        left = mergeSort(left)[2]
        right = mergeSort(right)[2]

        leftIterator, rightIterator, mainIterator  = 0, 0, 0
        ##while left value and right value are still indexs in the list
        while leftIterator < len(left) and rightIterator< len(right):
            ## Check if one number is less than or equal to the other
            if left[leftIterator] <= right[rightIterator]:
                ##Then sort it
                listSix[mainIterator] = left[leftIterator]
                leftIterator +=1
            
            else:
                listSix[mainIterator] = right[rightIterator]
                rightIterator +=1
            mainIterator +=1
            
        while leftIterator < len(left):
            listSix[mainIterator] = left[leftIterator]
            leftIterator +=1
            mainIterator +=1
            
        while rightIterator < len(right):
            listSix[mainIterator] = right[rightIterator]
            rightIterator +=1
            mainIterator +=1

    end = time.time()
    return (True, [start, end], listSix)

