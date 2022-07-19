def find_max_sum_sublist(lst):
    maxGlobal = lst[0]
    maxCurrent = lst[0]
    
    
    for i in range(1, len(lst)):
        maxCurrent = max(lst[i], lst[i] + maxCurrent)

        if maxGlobal < maxCurrent:
            maxGlobal = maxCurrent
    return maxGlobal
