def decryptor(Text, Key):
    #this function takes in a crypted text and its key as input arguments, and returns the decrypted form
    if(type(Text)!=str or type(Key)!= int):      #this ensures the text and key are of the right types
        return "Wrong argument type"
    else:
        upper_case="ABCDEFGHIJKLMNOPQRSTUVWSYZ"  #string containing all letters in uppercase 
        lower_case="abcdefghijklmnopqrstuvwxyz"  #string containing all letters in lowercase
        decrypted_text=""                        #an empty string that would contain the decrypted text
        for character in Text:                   #this loops through all the text in the string  
            if character in upper_case:          #for characters in upper case
                decrypted_text=decrypted_text+upper_case[(upper_case.find(character)+Key)%26] #this adds together each decrypted characters in
                #uppercase to form the decrypted text. The modulus operator helps ensure a loop of the string for characters to be taken in any
                #order. With this, indexing with any key wasnt a problem. after the key was added, the modulus was taken to determine the exact
                #index of the decrypted character.
            elif character in lower_case:        #for characters in lower case
                decrypted_text=decrypted_text+lower_case[(lower_case.find(character)+Key)%26]#this adds together each decrypted characters in
                #lowercase to form the decrypted text. Same concept as above  
            else:
                decrypted_text=decrypted_text+character                                         #this adds all nonalphabetic characters to the decrypted text
        return decrypted_text                                                                   #this returnss the decrypted text
print(decryptor("Rcb mjh 9 xo cqn 30 mjhb xo lxmn lqjuunwpn!!", 17))
print(decryptor("Sdwp zkaoj'p gehh ukq, iwgao ukq opnkjcan.", -22))

        
        
