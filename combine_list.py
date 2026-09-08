def combine_lists(list1, list2):
    return {key: value for key, value in zip(list1, list2)}

print(combine_lists(["a", "b", "c"], [1, 2, 3]))