# Topic: Dictionary Merging with Logic

# Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.

# Purpose: Real-world data often comes from multiple sources. Simply using dict.update() would overwrite duplicate keys. This exercise introduces you to efficient dictionary iteration and the dict.get(key, default) method, which is essential for avoiding KeyError.

# Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}

# Expected output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}

def dictionary_merger(dictionary1, dictionary2):
    merged_dictionary = {}

    

    return merged_dictionary

dictionary1 = {'a': 10, 'b': 20}
dictionary2 = {'b': 5, 'c': 15}

result = dictionary_merger(dictionary1, dictionary2)
print(result)
