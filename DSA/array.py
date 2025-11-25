def find_largest_brute_force(arr):
    pass

def largest_optimal(arr):
    if not arr:
        return None
    max_element = 0
    for num in arr:
        if num > max_element:
            max_element = num

    return max_element

arr = [3,5,1,2,9,7]
print(largest_optimal(arr))

def sec_largest_brute_force(arr):
    arr = set(arr)
    arr = list(arr)
    n = len(arr)
    if n < 2:
        return None
    
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] > arr[i]:
                count += 1
        if count == 1:
            return arr[i]
    return None

arr = [10,10,5,8,20,20]
print(sec_largest_brute_force(arr))    

def sec_largest_optimal(arr):
    if len(arr) > 2:
        return None
    
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

arr = [10,10,5,8,20,20]
print(sec_largest_optimal(arr))    

def sec_largest_optimal(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first>num>second:
            second = num
    return second if second != float('-inf') else None

