def heapify(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2

    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)


def add_to_heap(arr, value):
    arr.append(value)
    i = len(arr) - 1
    while i > 0:
        p = (i - 1) // 2
        if arr[p] < arr[i]:
            arr[p], arr[i] = arr[i], arr[p]
            i = p
        else:
            return arr
    return arr


def remove_from_heap(arr):
    root = arr[0]
    last = arr.pop()
    heapify(arr, 0, len(arr))


def built_heap(arr, n):
    start_ind = (n // 2) - 1

    for i in range(start_ind, -1, -1):
        heapify(arr, i, n)


def printHeap(arr):
    print("Array representation of Heap is:")
    n = len(arr)
    for i in range(n):
        print(arr[i], end=" ")
    print()


def is_max_heap(a):
    n = len(a)
    for i in range(n):
        l, r = 2 * i + 1, 2 * i + 2
        if l < n and a[i] < a[l]:
            return False
        if r < n and a[i] < a[r]:
            return False
    return True


if __name__ == "__main__":
    arr = [1, 3, 5, 6, 13, 10, 9, 8, 15, 17]

    n = len(arr)

    built_heap(arr, n)
    printHeap(arr)
    arr = add_to_heap(arr, 4)
    print(is_max_heap(arr))
