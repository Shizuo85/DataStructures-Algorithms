def find_minimum(arr):
    min_num = float("inf")
    print(min_num)
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num