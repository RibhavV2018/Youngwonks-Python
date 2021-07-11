from Sort import *
from Search import *
import time, random
l = [random.randint(0,1000) for i in range(10000)]
sortedL = [random.randint(0,1000) for i in range(10000)]
sortedL.sort()

def elapsedTime(results):
    if results:
        print(results[2])
        print('time elapsed: '+ str(results[1][1] - results[1][0]))
        print()
        print()
    else:
        print('No value found')


##Linear Search
elapsedTime(linearSearch(int(input('num')), l))
    

##Binary Search
elapsedTime(binarySearch(sortedL, int(input('num')), len(l), 0))

##Bubble Sort
elapsedTime(bubbleSort(l))

##selectionSort
elapsedTime(selectionSort(l))

##insertionSort
elapsedTime(insertionSort(l))
