def OddEven(n):
    """
    This function takes in a positive integer n and returns Evenish if the sum of its digits is even and oddish otherwise
    """
    assert type(n)==int and n>-1
    num=str(n); n=0
    for m in num:
        n=n+int(m)
    if n%2==0: return "Evenish"
    else: return "Oddish"
