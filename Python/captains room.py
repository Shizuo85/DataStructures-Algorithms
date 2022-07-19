def captains_room(lst):
    #this function takes in a list containing vales with several repeated, and returns the only value not repeated
    if(type(lst)!=list):
        return "Parameter must be a list"
    else:
        lst2=[]
        lst3=[]
        for i in range(len(lst)):
            n=1
            if(lst[i] in lst2):
                continue
            else:
                for k in range(i+1,len(lst)):
                    if(lst[i]==lst[k]):
                        lst2=lst2+[lst[i]]
                        break
                    else:
                        n=n+1
            while(n==len(lst)-i):
                lst3=lst3+[lst[i]]
                n=n+1
        if(len(lst3)!=1):
            print("Possible rooms for the captain are:",lst3, sep=" ")
            return "There's  an error in your list though,there should only be one captain"
        else:
            print("The captains room number is:", end=" ")
            return lst3[0]
print(captains_room([1,2,1,2,1,3,787,67,4,3,4,9,5,8,7,7,787,9,8,7,5,5,33,6,33,2,26]))
print(captains_room([1,2,1,2,1,3,787,4,3,4,9,5,8,7,7,787,9,8,7,5,5,33,33,2,26]))
