def reverse_list(lst):
    lst_length = len(lst)
    for i in range(lst_length):
        if i < lst_length - i - 1:
            temp = lst[i]
            lst[i] = lst[lst_length - i - 1]
            lst[lst_length - i - 1] = temp
        else:
            return lst


print(reverse_list([1, 2, 3, 4, 5, 6]))
