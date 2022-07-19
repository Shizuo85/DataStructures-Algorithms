N=int(input("Enter the number of digits required "))
number=str(10**(N-1)+1)
while int(number)<(10**N) and int(number)>(10**(N-1)):
    length= len(number)
    n=0
    lst= ['0','1','6','8','9']
    for i in number:
        if(i not in lst ):
            break
        else:
            if((i=='1' and number[n-1]=='1' or i=='0' and number[n-1]=='0' or i=='6' and number[n-1]=='9' or i=='9' and number[n-1]=='6' or i=='8' and number[n-1]=='8') and length>1):
                print('', end="")
            else:
                break
        n=n-1
        while (n+length)==0:
            print(number + " is a strobogrammatic number")
            n=n-1
    number=str(int(number)+1)
                
    
