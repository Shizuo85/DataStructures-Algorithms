def validate_email(email):
    #this function takes in an email address as a string and returns a string telling whether it is valid or not based on the conditions before
    #using someone@example.top_Domain as the email format, the string "someone" must not contain uppercase letters and can contain only a single dot
    #the string "example" must be in lower case and contain only alphanumeric and the hyphen
    #the string "top_Domain" can contain only alphabets and dots, and neither of the last two elements can be dots
    if type(email)!=str:
        #this checks if the argument is of the right type
        return "Invalid email"
    elif("@" not in email or "." not in email):
        #this checks whether the division between the three strings exist 
        return "Invalid email"
    else:
        not_someone="   ABCDEFGHIJKLMNOPQRSTUVWXYZ "                           #string of characcters not to be present in the someone string
        in_example="abcdefghijklmnopqrstuvwxyz0123456789-"                     #string of characters allowed in the example string
        in_topdomain="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz."   #string of characters allowed in the top_Domain string
        someone=email[:email.index("@")]                                       #this produces a string of characters just before "@" in email
        email=email[email.index("@"):]                                         #email is resigned to ignore the possible presence of "." in someone
        try:                                                                   #this is placed in a try clause for when "." does not exist after slicing
            example=email[email.index("@")+1:email.index(".")]                 #this produces a string of characters between "@" and "." in email
            top_Domain=email[email.index(".")+1:]                              #this produces the top_Domain string from the email string
        except:
            return "Invalid email"
        if(len(top_Domain)==0 or len(someone)==0 or len(example)==0):          #checks if all parts of the email is present         
            return "Invalid email"
        for character in someone:
            if character in not_someone:                                       #checks if someone has any unwanted character                                      
                return "Invalid email"
        for character in example:
            if character not in in_example:                                    #checks if example has any unwanted character
                return "Invalid email"
        for character in top_Domain:
            if character not in in_topdomain:                                  #checks if top_Domain has any unwanted character
                return "Invalid email"
        if(someone.count(".")>1):                                              #checks if someone has more than one "."
            return "Invalid email"
        elif("." in top_Domain):                                               
            if(top_Domain[::-1].index(".")>3):                                 #checks if top_domain has 2 or 3 characters after the last dot
                return "Invalid email"
        else:
            return "valid email"
        
print(validate_email("ekeneanthony85@gmail.com"))
