def merge_sorted_lists(list_of_sorted_lists):
    result = []
    
    while list_of_sorted_lists:
        min_vals = [lst[0] for lst in list_of_sorted_lists]
        min_index = min(range(len(min_vals)), key=min_vals.__getitem__)
        result.append(list_of_sorted_lists[min_index].pop(0))
        
        if not list_of_sorted_lists[min_index]:
            list_of_sorted_lists.pop(min_index)
    
    return result

# Example usage:
list_of_sorted_lists = [[1, 3, 6], [2, 4, 8], [5, 7, 9]]
sorted_list = merge_sorted_lists(list_of_sorted_lists)
print(sorted_list)
