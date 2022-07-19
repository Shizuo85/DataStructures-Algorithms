def bubble_sort(arr):
    """
    This function takes in an array arr and returns the number of steps taken to sort it using the bubble algorithm 
    """
    assert (type(arr)==list or type(arr)==set or type(arr)==tuple)
    a=2
    if type(arr)==tuple:
        a=0
        arr=list(arr)
    elif type(arr)==set:
        a=1
        arr=list(arr)
    for i in arr: assert type(i)==int
    count=0; n=0
    while  n!=len(arr):
        for i in range(1, len(arr)):
            if arr[i-1]>arr[i]:
                arr[i-1], arr[i]= arr[i], arr[i-1]
                count=count+1
        n=n+1
    if a==0: arr=tuple(arr)
    elif a==1: arr=set(arr)
    return count
