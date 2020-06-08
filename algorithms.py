################ Merge Sort ################
def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1
    return arr

################ Heap Sort ##########s######
def heap(arr):  
    def swap(first, index):  
        root = first  
        while root * 2 + 1 < index:  
            leaf = root * 2 + 1  
            if leaf < index - 1 and arr[leaf] < arr[leaf + 1]:  
                leaf += 1  
            if arr[root] < arr[leaf]:  
                arr[root], arr[leaf] = arr[leaf], arr[root]  
                root = leaf  
            else:  
                return    
    first = (len(arr) // 2 )- 1  
    last = len(arr) - 1  
    while first >= 0:  
        swap(first, len(arr))  
        first -= 1  
    while last > 0:  
        arr[last], arr[0] = arr[0], arr[last]  
        swap(0, last)  
        last -= 1
    return arr

################ Quick Sort ################		
def quick(arr, first, end, pivot):
    if end - first > 0:
        i = first - 1
        pivot = arr[end]
        for j in range(first, end):
            if arr[j] <= pivot:
                i = i + 1
                (arr[i], arr[j]) = (arr[j], arr[i])
        (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
        pivot = i + 1
        quick(arr, first, pivot - 1, pivot)
        quick(arr, pivot + 1, end, pivot)
    return arr
################ Quick Median Sort ################
def partition(arr,first,last):
    med = (last - 1 - first) // 2
    med = med + first
    left = first + 1
    if (arr[med] - arr[last-1])*(arr[first]-arr[med]) >= 0:
        arr[first],arr[med] = arr[med],arr[first]
    elif (arr[last - 1] - arr[med]) * (arr[first] - arr[last - 1]) >=0:
        arr[first],arr[last - 1] = arr[last - 1],arr[first]
    pivot = arr[first]
    for right in range(first,last):
        if pivot > arr[right]:
            arr[left],arr[right] = arr[right],arr[left]
            left = left + 1
    arr[first],arr[left-1] = arr[left-1],arr[first]
    return left-1
def quickMedian(arr,first,last):
    if first < last:
        splitPoint = partition(arr,first,last)
        quickMedian(arr,first,splitPoint)
        quickMedian(arr,splitPoint+1,last)
    return arr
    
    
################ Insertion Sort ################
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr

################ Selection Sort ################
def selection(arr):
    for i in range(len(arr)):
        minVal = min(arr[i:])
        indexMinVal = arr.index(minVal)
        arr[i], arr[indexMinVal] = arr[indexMinVal], arr[i]
    return arr

################ Bubble Sort ################
def bubble(arr):  
    for key in range(len(arr)-1, 0, -1):
        for i in range(key):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
################ Create display list ################
def displayList(sortedList,runtime,storage):
    dispList = []
    dispList.append(sortedList)
    dispList.append(runtime)
    dispList.append(storage)
    return dispList
################ Display Function ################
def Display(key,array):
    if key == "mainList":
        print("Orginal List:",array)
    elif key == "merge":
        print("List Sorted by MERGE Sort:",array[0])
        print("Time taken to sort using MERGE Sort:",array[1])
        print("Storage used to sort using MERGE Sort:",array[2])
    elif key == "heap":
        print("List Sorted by HEAP Sort:",array[0])
        print("Time taken to sort using HEAP Sort:",array[1])
        print("Storage used to sort using HEAP Sort:",array[2])
    elif key == "quick":
        print("List Sorted by QUICK Sort:",array[0])
        print("Time taken to sort using QUICK Sort:",array[1])
        print("Storage used to sort using QUICK Sort:",array[2])
    elif key == "quickMed":
        print("List Sorted by QUICK Sort with MEDIAN:",array[0])
        print("Time taken to sort using QUICK Sort with MEDIAN:",array[1])
        print("Storage used to sort using QUICK Sort with MEDIAN:",array[2])
    elif key == "insert":
        print("List Sorted by INSERTION Sort:",array[0])
        print("Time taken to sort using INSERTION Sort:",array[1])
        print("Storage used to sort using INSERTION Sort:",array[2])
    elif key == "bubble":
        print("List Sorted by BUBBLE Sort:",array[0])
        print("Time taken to sort using BUBBLE Sort:",array[1])
        print("Storage used to sort using BUBBLE Sort:",array[2])
    elif key == "select":
        print("List Sorted by SELECTION Sort:",array[0])
        print("Time taken to sort using SELECTION Sort:",array[1])
        print("Storage used to sort using SELECTION Sort:",array[2])
        
def boxmessage(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)