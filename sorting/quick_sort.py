def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def _quick_sort(low, high):
        if low >= high:
            return
        pivot_index = partition(low, high)
        _quick_sort(low, pivot_index - 1)
        _quick_sort(pivot_index + 1, high)

    _quick_sort(0, len(arr) - 1)
    return arr


def sort_with_quick(arr):
    quick_sort(arr)
    return arr


print(sort_with_quick([3, 1, 4, 1, 5, 9]))  # -> [1, 1, 3, 4, 5, 9]
print(sort_with_quick([10, 9, 8, 7, 6, 5]))  # -> [5, 6, 7, 8, 9, 10]
print(sort_with_quick([5, 5, 5, 5]))  # -> [5, 5, 5, 5]
print(sort_with_quick([42]))  # -> [42]
print(sort_with_quick([]))  # -> []
