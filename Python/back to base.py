def to_base(num, base):
    """
    This funtion takes in two integers, first a number in decimal, then a base to convert the number to and returns a string of the converted number
    """
    assert type(num)==int and type(base)==int and base in [2, 4, 8, 16] and num>-1
    dict1={0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
    n=0
    Num=abs(num)
    base_equivalent=""
    while Num>=base**(n+1):
        n=n+1
    while n>-1:
        for i in range(base-1, -1, -1):
            if Num-i*base**n>=0:
                base_equivalent=base_equivalent+dict1[i]
                break
            else:
                continue
        Num=Num-i*base**n
        n=n-1
    return base_equivalent if num>=0 else "-"+base_equivalent
