def k_largest(arr, k):
    """
    This function takes in an array arr and an integer k and returns the kth largest element in the array
    """
    assert (type(arr)==list or type(arr)==set or type(arr)==tuple) and type(k)==int and k>0 and k<=len(arr)
    if type(arr)!=list: arr=list(arr)
    for i in range(len(arr)):
        assert type(arr[i])==int
        count=0
        for m in range(len(arr)):
            assert type(arr[m])==int
            if arr[i]<arr[m]:
                count=count+1
            else:
                continue
        if count==k-1:
            return arr[i]
