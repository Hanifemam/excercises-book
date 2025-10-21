def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr), 1):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


print(bubble([2, 5, 4, 3, 9]))
