def selection_sort(arr):
    for i in range(len(arr)):
        max = 0
        for j in range(0, len(arr) - i, 1):
            if arr[j] > arr[max]:
                max = j
        temp = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = arr[max]
        arr[max] = temp
    return arr


print(selection_sort([2, 5, 4, 3, 9]))
