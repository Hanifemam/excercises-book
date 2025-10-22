def merge_sort(arr, left, right):
    if left >= right:
        return arr

    # splitting
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    # Merging
    i = left
    j = mid + 1
    merged = []
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1
    merged.extend(arr[i : mid + 1])
    merged.extend(arr[j : right + 1])
    arr[left : right + 1] = merged


def sort_with_merge(arr):
    merge_sort(arr, 0, len(arr) - 1)
    return arr


print(sort_with_merge([3, 1, 4, 1, 5, 9]))  # -> [1, 1, 3, 4, 5, 9]
print(sort_with_merge([10, 9, 8, 7, 6, 5]))  # -> [5, 6, 7, 8, 9, 10]
print(sort_with_merge([5, 5, 5, 5]))  # -> [5, 5, 5, 5]
print(sort_with_merge([42]))  # -> [42]
print(sort_with_merge([]))  # -> []
