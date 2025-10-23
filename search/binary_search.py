def binary_search(sorted_list, item, start, end):
    if end <= start:
        return False
    mid = (start + end) // 2
    if sorted_list[mid] == item:
        return True
    if sorted_list[mid] > item:
        return binary_search(sorted_list, item, start, mid - 1)
    else:
        return binary_search(sorted_list, item, mid + 1, end)


arr = [1, 2, 3, 4, 6, 7]
print(binary_search(arr, 5, 0, len(arr) - 1))
