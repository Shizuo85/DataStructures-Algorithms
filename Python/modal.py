def f(arr):
  """
  This function takes in a list as an argument and prints the modal
  value(s) amd a list containing only unique elements from the
  argument
  """
  if len(arr)==0: print("The unique list and modal list is given as: ", [])
  
  dct= {}
  lst1=[]
  lst2=[]
  max=0
  
  for i in arr:
    dct[i]=dct.get(i, 0)+1 #this creates a dictionary of elements and modal values
    if dct[i]==1: lst1.append(i) #this creates a unique list
    if dct[i]>max: max=dct[i] #this finds the max nuber of occurence
      
  print("The unique set is:",lst1)
  
  for k, v in dct.items():
    if v==max: lst2.append(k) #this creates a list modal elements
      
  if len(lst2)==1: print("The modal value is:", lst[0])
  else: print("The modal values are:", lst2)


lst= ["a", "b", "a", "a", 3, 3, 2, 3, "hello", "b"]
f(lst)