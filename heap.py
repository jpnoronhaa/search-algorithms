import time

comparisons = 0
assignment = 0


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
    

def heapSort(arr, type):
    start = time.time()
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)

    end = time.time()
    total_time = end - start

    if type == 'time':
        return total_time
    elif type == 'comparisons':
        return comparisons
    elif type == 'assignments':
        return assignment
