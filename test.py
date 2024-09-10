def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0]+recursive_sum(arr[1:])

# print(recursive_sum([1,1,4,5]))

def recursive_len(arr):
    if len(arr) == 1:
        return 1
    return 1 + recursive_len(arr[1:])
# print(recursive_len([1,1,4,5]))

def recursive_max(arr):
    if len(arr) == 1:
        return arr[0]
    return max(arr[0], recursive_max(arr[1:]))

# print(recursive_max([1,4,5,2,1]))

def recursive_search(guess, arr):
    return 0