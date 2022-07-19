import math
def faithful(n):
    #This function takes in a value n, and returns the nth term of the faithful number series
    lst=[]
    if(n<1):
        return "Number cant be less than one"
    else:
        for i in range(int(math.log(n,2))+1):
            lst.append(7**i)
            if(i>0):
                for m in range((2**i)-1):
                    lst.append(7**i+lst[m])
        lst.sort
        return lst[n-1]
#print(faithful(100))

