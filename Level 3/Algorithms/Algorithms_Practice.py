import time
import random

LIST = [random.randint(1,100) for i in range(20000)]

##Linear Search
def linearSearch(listOne, x):
  
    for i in range(len(listOne)):
  
        if listOne[i] == x:
            return i
  
    return "No match found"
start = time.time()
print(linearSearch([1,3,2,5,3,2,5,3,5,3,2,5,7,2,3,5,2,6,2],6))
end = time.time()
print("elapsed time: " + str(end-start))
print()
print()

##Bianary Search
def binarySearch(listTwo,x, high, low):
    if high>=low:
        mid = (high + low)//2
        if listTwo[mid] == x:
            return mid
        elif listTwo[mid] > x:
            return binarySearch(listTwo, x, mid-1, low)
        elif listTwo[mid] < x:
            return binarySearch(listTwo, x, high, mid+1)
    else:
        return "List Nonexistent"

start = time.time()
print(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19], 18, 18, 0))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()

##Bubble Sort
def bubbleSort(listThree):
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
                
    return listThree
'''
start = time.time()
print(bubbleSort(LIST))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()
'''
##Selection Sort
def selectionSort(listFour):
    smallestNum = 0
    for i in range(len(listFour)):
        for x in range(i + 1, len(listFour)):
            if listFour[smallestNum] > listFour[x]:
                smallestNum = x

        listFour[i], listFour[smallestNum] = listFour[smallestNum], listFour[i]
    return listFour
'''
start = time.time()
print(selectionSort(LIST))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()
'''      
##Insertion Sort

def insertionSort(listFive):
    for i in range(1, len(listFive)):
        key = listFive[i]
        numLess = i-1
        while numLess >=0 and key < listFive[numLess]:
            listFive[numLess+1] = listFive[numLess]
            numLess -= 1
        listFive[numLess+1] = key
    return listFive



start = time.time()
print(insertionSort(LIST))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()

    



