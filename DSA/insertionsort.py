def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted in the sorted part
        j = i - 1

        # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Move element one step right
            j -= 1

        arr[j + 1] = key  # Insert the key at the correct position

    return arr


arr = [9, 5, 1, 4, 3]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)


