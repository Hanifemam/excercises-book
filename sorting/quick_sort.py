def quick_sort(arr):
    pivot = arr[len(arr) - 1]
    pivot_ind = len(arr) - 1
    i = 0
    while i < len(arr) - 1 and i < pivot_ind:
        if arr[i] > pivot:
            arr[pivot_ind] = arr[i]
            arr[i] = arr[pivot_ind - 1]
            arr[pivot_ind - 1] = pivot
            pivot_ind -= 1
        else:
            i += 1
    quick_sort(arr[0 : pivot_ind - 1])
    quick_sort(arr[pivot_ind + 1 : len(arr) - 1])


def sort_with_quick(arr):
    quick_sort(arr)
    return arr


print(sort_with_quick([3, 1, 4, 1, 5, 9]))  # -> [1, 1, 3, 4, 5, 9]
print(sort_with_quick([10, 9, 8, 7, 6, 5]))  # -> [5, 6, 7, 8, 9, 10]
print(sort_with_quick([5, 5, 5, 5]))  # -> [5, 5, 5, 5]
print(sort_with_quick([42]))  # -> [42]
print(sort_with_quick([]))  # -> []
