def to_mandarin(num):
    """
    This function takes in an integer betwen 0 and 100 and returns its mandarin version as a string
    """
    if type(num)!=int:      #ensures the right type oof argument is inputted
        return "Wrong argument type"

    elif num<1 or num>99:   #ensures only the numbers within the range are inputted
        return "Number out of range"
    else:
        mandarin ={0: "", 1:"Yi", 2:"Er", 3:"San", 4:"Si", 5:"Wu", 6:"Liu", 7:"Qi", 8:"Ba", 9:"Jiu", 10:"Shi"}
        #a dictionary containing  some mandarin numbers and zero as an empty string  
        unit=num%10  
        tense=num//10
        if num<=10:              #1-10 follows the pattern of directly representing the number
            mandarin_num=mandarin[num]
        elif num>10 and num<20:  #11-19 follows the pattern of joining the madarin version of 10 and the unit digit 
            mandarin_num= mandarin[10] + " " + mandarin[unit]
        else:                    #20-99 follows the pattern of joining the madarin version of the tense digit, 10 and the unit digit 
            mandarin_num=mandarin[tense] + " " + mandarin[10] + " " + mandarin[unit]
        return mandarin_num
for i in range(100):
    print(i, to_mandarin(i), sep=" ")
        
