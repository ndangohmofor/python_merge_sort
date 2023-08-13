from random import shuffle


def qs(arr):
    if len(arr) <= 1:
        return arr

    smaller = []
    larger = []

    pivot = 0
    pivot_element = arr[pivot]

    for i in range(1, len(arr)):
        if arr[i] > pivot_element:
            larger.append(arr[i])
        else:
            smaller.append(arr[i])

    sorted_smaller = qs(smaller)
    sorted_larger = qs(larger)

    return sorted_smaller + [pivot_element] + sorted_larger


list = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(list)
print("PRE SORT: ", list)
print(qs(list))
# print("POST SORT: ", list)
