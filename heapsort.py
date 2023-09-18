from max_heap import MaxHeap


def heapsort(lst):
    sort = []
    max_heap = MaxHeap()
    for el in lst:
        max_heap.add(el)
    print(max_heap.retrieve_max())


my_list = [99, 22, 61, 10, 21, 13, 23, 44, 200, 54]
sorted_list = heapsort(my_list)
