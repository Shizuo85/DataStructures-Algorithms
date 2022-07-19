def loop_read(array):
    """
    This function takes in a matrix represented as a list of lists and returns a string of elements traced by going in a clockwise direction 
    """
    assert (type(array)==list or type(array)==tuple or type(array)==set) and len(array)>0
    if len(array[0])==0: return ""
    char=0; num=0; check=len(array[0])*len(array)
    for i in array:
        assert(type(i)==list or type(i)==tuple or type(i)==set) and check==len(i)*len(array)
        for k in i:
            assert type(k)==int or type(k)==str
            if type(k)==int: num=num+1
            elif type(k)==str: char=char+1
    assert char==check or num==check
    
    a=0; b=0; lst=[(a, b)]; string=str(array[a][b]); count=1
    while count!=check:
        while (a, b+1) not in lst:
            if b+1<len(array[0]): b=b+1
            else: break
            string=string+" "+str(array[a][b]); count= count+1
            lst.append((a,b))
        while (a+1, b) not in lst:
            if a+1<len(array):a=a+1
            else: break
            string=string+" "+str(array[a][b]); count= count+1
            lst.append((a,b))
        while (a, b-1) not in lst:
            if b-1>-1: b=b-1
            else: break
            string=string+" "+str(array[a][b]); count= count+1
            lst.append((a,b))  
        while (a-1, b) not in lst:
            if a-1>-1:a=a-1
            else: break
            string=string+" "+str(array[a][b]); count= count+1
            lst.append((a,b))
    return string

def rotate(arr):
    """
    This function takes in a square matrix represented as a list of lists and returns the same matrix rotated 90  degrees
    """
    assert (type(arr)==list or type(arr)==tuple or type(arr)==set) and len(arr)>0
    if type(arr)!=list: arr=list(arr)
    length=len(arr)
    for i in arr:
        assert type(i)==list and len(i)==length
        for k in i:
            assert type(k)==int
        arr=arr+[[]]
    for i in range(length-1, -1, -1):
        for k in range(length):
            arr[length+k].append(arr[i][k])
    for i in range(length):
        arr.pop(0)
