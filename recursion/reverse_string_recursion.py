def reverse(str):
    n = len(str)
    if n == 1:
        return str[0]
    return reverse(str[1:]) + str[0]


print(reverse("hanif"))
