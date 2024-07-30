import copy

original = [1, [2, 3], 4]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

print (shallow_copy, deep_copy)