
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i element will be sorted in the first i iteration
        for j in range(0, n-i-1): 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: # If no two elements were swapped in the inner loop, then break
            break
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 23]
    print("Unsorted array:", arr)
    sorted_arr = bubbleSort(arr)
    print("Sorted array:", sorted_arr)
