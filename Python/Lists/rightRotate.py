def right_rotate(lst, k):
    if len(lst):
        k=k%len(lst)
        return lst[-k:] + lst[:-k]
    return lst