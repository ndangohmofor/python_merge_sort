from random import randrange, shuffle


def quicksort(list, start, end):
    # This portion of the list has been sorted
    if start > end:
        return

    print("Running quicksort on {0}".format(list[start:end + 1]))
    # select a random element to act as the pivot of the list
    pivot_idx = randrange(start, end + 1)
    pivot_elemment = list[pivot_idx]
    print("Selected pivot {0}".format(pivot_elemment))

    # swap random element with last element in sub-lists
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # Track all the elements which should be to the left (lesser than) pivot
    lesser_than_pointer = start

    for i in range(start, end):
        # When we find an element out of place
        if list[i] < pivot_elemment:
            print("Swapping {0} with {1}".format(list[i], list[lesser_than_pointer]))
            list[i], list[lesser_than_pointer] = list[lesser_than_pointer], list[i]

            # tally that we have one more lesser element
            lesser_than_pointer += 1

    # move pointer element to the right-most portion of lesser elements
    list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]
    print("{0} successfully partitioned".format(list[start: end + 1]))
    #     recursively sort left and right sub-lists
    quicksort(list, start, lesser_than_pointer - 1)
    quicksort(list, lesser_than_pointer + 1, end)

list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)