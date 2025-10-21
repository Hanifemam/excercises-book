# Space O(n)
def insertion_sort(arr):
    insertion_arr = []
    insertion_arr.append(arr[0])
    for i in range(1, len(arr)):
        curr = arr[i]
        for j in range(len(insertion_arr)):
            if curr < insertion_arr[j]:
                insertion_arr.insert(j, curr)
                break
            if j == len(insertion_arr) - 1:
                insertion_arr.append(curr)

    return insertion_arr


print(insertion_sort([2, 5, 4, 3, 3, 9, 1]))


# Space O(1)
def insertion_sort_eff(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


print(insertion_sort_eff([2, 5, 4, 3, 3, 9, 1]))
