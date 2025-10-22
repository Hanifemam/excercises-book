def merge_sort(arr, right, left):
    if len(arr[right:left]) <= 1:
        return arr

    mid = (left - right) // 2
    left_arr = merge_sort(arr, left, mid)
    right_arr = merge_sort(arr, mid + 1, right)
