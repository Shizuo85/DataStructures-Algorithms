def sparsify(adj_dict):
    """
    This function takes in an adjacent dictionary and returns its sparse matrix 
    """
    assert type(adj_dict)==dict
    lst=[]
    for k, v in adj_dict.items():
        assert type(v)==dict and type(k)==str and k.isupper() and len(k)==1
        for x,y in v.items():
            assert type(x)==str and type(y)==int and x.isupper() and len(x)==1
        lst.append(k)
    for v in adj_dict.values():
        for x,y in v.items():
            assert type(x)==str and type(y)==int and x in lst
    lst.sort()
    sparse_matrix=[]
    for i in range(len(adj_dict)):
        sparse=[0]*len(adj_dict)
        for k, v in adj_dict.items():
            if lst[i] in v:
                sparse[lst.index(k)]=v[lst[i]]
        sparse_matrix.append(sparse)
    return sparse_matrix
print(sparsify({"A":{"B":1, "E":2}, "B":{"C":2}, "E":{"C": 2}, "C":{"A":1, "D":1}, "D":{}}))
