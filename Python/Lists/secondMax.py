def find_second_maximum(lst):
   lst=list(set(lst))
   if len(lst)>1:
      Max = lst[0]
      secondMax= lst[1]
      for i in lst:
         if i>Max:
            secondMax=Max
            Max=i
         elif i>secondMax and i<Max:
            secondMax=i
      return secondMax

   else:
      return None


