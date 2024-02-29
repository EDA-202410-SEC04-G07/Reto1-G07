from Estructuras import Lista as lis
            
MIN_MERGE = 32
  
  
def calcMinRun(n): 
    """Returns the minimum length of a 
    run from 23 - 64 so that 
    the len(array)/minrun is less than or 
    equal to a power of 2. 
  
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33, 
    ..., 127=>64, 128=>32, ... 
    """
    r = 0
    while n >= MIN_MERGE: 
        r |= n & 1
        n >>= 1
    return n + r 
  
  
# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertionSort(arr, sort_crit, left, right, tipo):
    size = lis.size(arr) 
    while left <= size:
        right =left
        while (right > 1) and (sort_crit(lis.getElement(arr, right,tipo),lis.getElement(arr, right-1,tipo))): 
            lis.exchange(arr, right,right-1,tipo)
            right -= 1
        left += 1
    return arr
  
# Merge function merges the sorted runs 
def merge(arr, sort_crit,  l, m, r, tipo): 
  
    # original array is broken in two parts 
    # left and right array 
    leftlist = lis.sub_list(arr,l,m,tipo)
    rightlist = lis.sub_list(arr,m+1,r-m,tipo)

    sort(leftlist, sort_crit, tipo)
    sort(rightlist, sort_crit, tipo)
  
    i = j = k = 1

    leftelements = lis.size(leftlist)
    rightelements = lis.size(rightlist)
    # after comparing, we merge those two array 
    # in larger sub array 
    while (i <= leftelements)  and (j < rightelements): 
        elemi = lis.getElement(leftlist,i, tipo)
        elemj = lis.getElement(rightlist, j, tipo)

        if sort_crit(elemj,elemi): 
            lis.changeInfo(arr,k,elemj, tipo)
            j += 1
  
        else: 
            lis.changeInfo(arr,k,elemi, tipo)
            i += 1
  
        k += 1
  
    # Copy remaining elements of left, if any 
    while i <= leftelements: 
        lis.changeInfo(arr,k,lis.getElement(leftlist, i, tipo), tipo) 
        i += 1
        k += 1
  
    # Copy remaining element of right, if any 
    while j <= rightelements: 
        lis.changeInfo(arr,k,lis.getElement(rightlist, j, tipo), tipo) 
        j += 1
        k += 1
    return arr
  
# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def sort(arr,sort_crit, tipo): 
    n = len(arr) 
    minRun = calcMinRun(n) 
  
    # Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr,sort_crit, start, end, tipo) 
  
    # Start merging from size RUN (or 32). It will merge 
    # to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 
  
        # Pick starting point of left sub array. We 
        # are going to merge arr[left..left+size-1] 
        # and arr[left+size, left+2*size-1] 
        # After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 
  
            # Find ending point of left sub array 
            # mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
  
            # Merge sub array arr[left.....mid] & 
            if mid < right: 
                merge(arr,sort_crit, left, mid, right, tipo) 
  
        size = 2 * size 
    return arr