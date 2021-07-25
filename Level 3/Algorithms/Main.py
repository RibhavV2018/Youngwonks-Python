from Sort import *
from Search import *
import time, random
l = [random.randint(0,1000) for i in range(1000)]
sortedL = [random.randint(0,1000) for i in range(1000)]
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
print("Linear Search")
elapsedTime(linearSearch(int(input('num')), l))
##    
##
####Binary Search
print("Binary Search")
elapsedTime(binarySearch(sortedL, int(input('num')), len(sortedL), 0))
##
####Bubble Sort
print("Bubble Sort")
elapsedTime(bubbleSort(l))
##
####selectionSort
print("Selection Sort")
elapsedTime(selectionSort(l))

##insertionSort
print("Insertion Sort")
elapsedTime(insertionSort(l))

##Merge Sort
print("Merge Search")
elapsedTime(mergeSort(l))
