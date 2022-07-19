def find_product(lst):

    product=1
    Zero=0
    productZero=1
    for num in lst:
        product *= num
        if num != 0 :
            productZero *=num
        else:
            Zero+=1

    for i in range(len(lst)):
         if lst[i] != 0: lst[i] = product/lst[i]
         elif Zero<2: lst[i] = productZero 

    return lst