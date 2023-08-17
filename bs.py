def bubble_sort(arr, comparison_function):
    swaps = 0
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                sorted = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print("Bubble sort: There were {0} swaps".format(swaps))
    return arr