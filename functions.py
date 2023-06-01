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
    

def heap_sort(arr, type):
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


def bubbleSort(arr, type):
    start = time.time()
    size = len(arr)
    comparisons = 0
    assignment = 0

    for i in range(size - 1):
        for j in range(size - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                assignment += 1
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    end = time.time()
    total_time = end - start

    if type == 'time':
        return total_time
    elif type == 'comparisons':
        return comparisons
    elif type == 'assignments':
        return assignment

def insertion_sort(arr ,type):
    start = time.time()
    comparisons = 0
    assignment = 0

    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > chave:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignment += 1
            j -= 1

        arr[j + 1] = chave
    end = time.time()
    total_time = end - start

    if type == 'time':
        return total_time
    elif type == 'comparisons':
        return comparisons
    elif type == 'assignments':
        return assignment
    
def merge_sort(arr , type):
    start = time.time()
    comparisons = 0
    assignments = 0
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        comparisons += merge_sort(left_half)
        comparisons += merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                assignments += 1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    end = time.time()
    total_time = end - start

    if type == 'time':
        return total_time
    elif type == 'comparisons':
        return comparisons
    elif type == 'assignments':
        return assignment

def quick_sort(arr, type):
    start = time.time()
    comparisons = 0
    assignments = 0
    
    if len(arr) <= 1:
        return comparisons + assignments
    
    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    comparisons += len(arr) - 1
    assignments += len(arr)
    
    comparisons += quick_sort(smaller)
    comparisons += quick_sort(greater)
    
    arr[:] = smaller + equal + greater
    
    end = time.time()
    total_time = end - start

    if type == 'time':
        return total_time
    elif type == 'comparisons':
        return comparisons
    elif type == 'assignments':
        return assignment

def gnome_sort(arr, type):
    start = time.time()
    comparisons = 0
    assignments = 0
    
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
            comparisons += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            comparisons += 2
            assignments += 1
    end = time.time()
    total_time = end - start      

    if type == 'time':
        return total_time
    elif type == 'comparisons':
        return comparisons
    elif type == 'assignments':
        return assignment

def selection_sort(arr, type):
    start = time.time()
    comparisons = 0
    assignments = 0
    
    for i in range(len(arr)):
        min_index = i
        
        for j in range(i+1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 1
            
    end = time.time()
    total_time = end - start      

    if type == 'time':
        return total_time
    elif type == 'comparisons':
        return comparisons
    elif type == 'assignments':
        return assignment