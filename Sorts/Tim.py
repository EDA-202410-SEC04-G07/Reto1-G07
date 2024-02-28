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
def insertionSort(arr, sort_crit, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and sort_crit(lis.getElement(arr, j),lis.getElement(arr, j-1)): 
            lis.exchange(arr, j,j-1)
            j -= 1
  
# Merge function merges the sorted runs 
def merge(arr, sort_crit,  l, m, r): 
  
    # original array is broken in two parts 
    # left and right array 
    len1, len2 = m - l + 1, r - m 
    left, right = [], [] 
    for i in range(0, len1): 
        left.append(lis.getElement(arr,l + i))
    for i in range(0, len2): 
        right.append(lis.getElement(arr,m + 1 + i))
  
    i, j, k = 0, 0, l 
  
    # after comparing, we merge those two array 
    # in larger sub array 
    while i < len1 and j < len2: 
        if sort_crit(left[i],right[j]): 
            lis.changeInfo(arr,k,left[i])
            i += 1
  
        else: 
            lis.changeInfo(arr,k,right[j])
            j += 1
  
        k += 1
  
    # Copy remaining elements of left, if any 
    while i < len1: 
        lis.changeInfo(arr,k,left[i]) 
        k += 1
        i += 1
  
    # Copy remaining element of right, if any 
    while j < len2: 
        lis.changeInfo(arr,k,right[j])
        k += 1
        j += 1
  
  
# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def sort(arr,sort_crit): 
    n = len(arr) 
    minRun = calcMinRun(n) 
  
    # Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr,sort_crit, start, end) 
  
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
                merge(arr,sort_crit, left, mid, right) 
  
        size = 2 * size 
    return arr