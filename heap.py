# from pygnuplot import  gnuplot
import time
import json
import argparse

parser = argparse.ArgumentParser()                                               
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()
filename = args.file

file = open(filename)
data = json.load(file)

comparisons = 0
assignment = 0

start = time.time()

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    global comparisons
    global assignment

    comparisons += 1
    if l < n and arr[i] < arr[l]:
        assignment += 1
        largest = l

    comparisons += 1
    if r < n and arr[largest] < arr[r]:
        assignment += 1
        largest = r

    comparisons += 1
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)
    

def heapSort(arr):
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)

arr = data['ascending']

heapSort(arr)

end = time.time()
total_time = end - start

print(arr)
print(comparisons)
print(assignment)
print(total_time)

