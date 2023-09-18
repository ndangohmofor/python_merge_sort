from max_heap import MaxHeap


def heapsort(lst):
    sort = []
    max_heap = MaxHeap()
    for el in lst:
        max_heap.add(el)
    # print(max_heap.retrieve_max())

    while max_heap.count > 0:
        sort.insert(0, max_heap.retrieve_max())
    return sort


my_list = [99, 22, 61, 10, 21, 13, 23, 44, 200, 54, 97, 202]
sorted_list = heapsort(my_list)
print(sorted_list)