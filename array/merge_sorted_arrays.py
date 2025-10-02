def merge_sorted_array(arr1, arr2):
    merged_array = []
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    arr1_ind, arr2_ind = 0, 0
    while arr1_ind < arr1_len and arr2_ind < arr2_len:
        if arr1[arr1_ind] < arr2[arr2_ind]:
            merged_array.append(arr1[arr1_ind])
            arr1_ind += 1
        else:
            merged_array.append(arr2[arr2_ind])
            arr2_ind += 1
    if arr1_ind < arr1_len:
        for i in range(arr1_ind, arr1_len):
            merged_array.append(arr1[i])
    else:
        for i in range(arr2_ind, arr2_len):
            merged_array.append(arr2[i])
    return merged_array


print(merge_sorted_array([1, 3, 5, 7], [2, 4, 6, 8]))
