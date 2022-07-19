def my_exes(matrix, thresh=None):
    """
    This function takes in a matrix represented as a list of lists and an optional variable thresh and returns the number of Xs in the matrix
    """
    
    assert type(matrix)==list and len(matrix)>0
    
    for i in range(len(matrix)):
        assert type(matrix[i])==list and len(matrix[i])==len(matrix[0])
        for k in range(len(matrix[i])): assert matrix[i][k]==0 or matrix[i][k]==1

    assert thresh==None or (type(thresh)==int and thresh>0 ) 

    n=1; count=0 
    for w in range(min(len(matrix), len(matrix[0]))):
        for i in range(len(matrix)-n):
            for k in range(len(matrix[0])-n):
                a=0
                for m in range(n+1):
                    if matrix[i+m][k+m]==1 and matrix[i+m][k+n-m]==1: a=a+1
                if a==n+1: count=count+1
        if type(thresh)==int and n==thresh: break
        else: n=n+1
        
    return count
