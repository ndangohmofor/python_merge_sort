def parent_idx(idx):
    return idx // 2


def left_child_idx(idx):
    return idx * 2


def right_child_idx(idx):
    return (idx * 2) + 1


class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while parent_idx(idx) > 0:
            element = self.heap_list[idx]
            parent = self.heap_list[parent_idx(idx)]
            if parent < element:
                print("Swapping {0} with {1}".format(parent, element))
                self.heap_list[parent_idx(idx)] = element
                self.heap_list[idx] = parent
            idx = parent_idx(idx)
        print("Heap Restored {0}".format(self.heap_list))

    def child_present(self, idx):
        return left_child_idx(idx) <= self.count

    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None
        max_val = self.heap_list[1]
        print("Removing [{0}] from [{1}]".format(max_val, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: [{0}]".format(self.heap_list))
        return max_val
