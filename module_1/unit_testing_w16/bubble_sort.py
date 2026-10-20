def bubble_sort(list_to_sort):
    if not list_to_sort:
        raise TypeError(f'List is empty. Closing program')
    if not isinstance(list_to_sort, list):
        raise TypeError("Input must be a list")
    for outer_index in range(0, len(list_to_sort) - 1):
        made_change = False
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            current_item = list_to_sort[index]
            next_item = list_to_sort[index - 1]
            print(f'-- Index {index}. Current Item: {current_item}, Next Item: {next_item}')
            if current_item < next_item:
                print("changing items ")
                list_to_sort[index] = next_item
                list_to_sort[index - 1] = current_item
                made_change = True
        if not made_change:
            return list_to_sort
    return list_to_sort

test_list = [87, 35, 14, 42, 93, 7]
bubble_sort(test_list)
print(test_list)