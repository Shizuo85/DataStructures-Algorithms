def key_pressed(text):
    """
    This function takes in a text as a string and returns the key presses  that must be made tto enter the text as a string
    """
    if type(text)!=str:
        return "Invalid argument"
    text=text.upper()
    Dict={1:".,?!:", 2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ", 0:" "}
    #a dictionary containinig the keys an keys and symbols as values
    num=""
    for char in text:
        #For each character in the text, the items of the dictionary is looped through to check for the  character in each value
        check=0 #this is used to check if a character exists in the dictionary by counting the number of times it isn't found in a key
        for key,value in Dict.items():
            if(char in value):
                #(index of the char+1)number of the key of the corresponding value where the letter is located is added to the num string
                num=num+str(key)*(value.index(char)+1)
                break
            else:
                #for each time the character isn't found, check increases by 1
                check=check+1
            if check==10:
                return "Invalid string"    
    return num
print(key_pressed("Hello, World!"))
