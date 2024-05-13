def concatenate_dicts(*dicts):
    new_dict = {}
    for d in dicts:
        new_dict.update(d)
    return new_dict

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

concatenated_dict = concatenate_dicts(dict1, dict2, dict3)
print(concatenated_dict)