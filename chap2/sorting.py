

class Sorting:
    """Class for sorting an array.

    Attribute:
        array (list): the array to be sorted
    Methods:
        insertion_sort: sort the array
    """

    def __init__(self, array):
        """Initialize the class

        Args:
            array (list): list to be sorted
        """
        self.array = array

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        return self.array

    def merge_sort_wraper(self):
        self.merge_sort(self.array)

    def merge_sort(self, arr):
        if len(arr) > 1:
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
            left_index = 0
            right_index = 0
            new_index = 0
            while left_index < len(left_arr) and right_index < len(right_arr):
                if left_arr[left_index] <= right_arr[right_index]:
                    arr[new_index] = left_arr[left_index]
                    left_index += 1
                elif right_arr[right_index] <= left_arr[left_index]:
                    arr[new_index] = right_arr[right_index]
                    right_index += 1
                new_index += 1
            while left_index < len(left_arr):
                arr[new_index] = left_arr[left_index]
                left_index += 1
                new_index += 1
            while right_index < len(right_arr):
                arr[new_index] = right_arr[right_index]
                right_index += 1
                new_index += 1
            
