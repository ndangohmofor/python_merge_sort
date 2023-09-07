def binary_search(sorted_list, left_pointer, right_pointer, target):
    # this condition indicates we have reached an empty sublist
    if left_pointer >= right_pointer:
        return "value not found"

    # calculate the middle index from the pointers
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx

    if mid_val > target:
        # reduce the list by considering only the left side => change the right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)

    if mid_val < target:
        # reduce the list by considering only the right side => change the left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))

