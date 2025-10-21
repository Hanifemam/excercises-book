def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubble([2, 5, 4, 3, 9]))
