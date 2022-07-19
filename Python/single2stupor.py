def single2stupor(n):
    """
    This function takes in a positive integer n and returns its nummber of persistence
    """
    type(n)==int, "Invalid"
    assert n>-1, "Wrong input"
    num=str(n); count=0
    while n>9:
        n=1
        for m in num:
            n=n*int(m)
        num=str(n)
        count=count+1
    return count
