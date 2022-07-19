def Hangman(word, trials):
    """this function takes in a string which is the secret word to be guessed and the number of trials allowed as arguments.
    It first ensures the right argument types are entered. Afterwards it converts the string to lowercase to avoid difference
    in case error. The string is then represented as a list for easy manipulation"""
    if(type(word)!=str or type(trials)!=int):
        return "Wrong argument type"
    else:
        word=word.lower()   #ensures the program isnt case sensitive
        word=list(word)     #assigns a list to word containing all letters in the secret word as elements
        guessed=[]          #a new list where guessed numbers will be stored
        while(len(word)!=len(guessed) and trials!=0):   #this continues to loop until all the letters are guessed or all the trials are exhausted
            guess=(input("Guess a letter in the  word: ")).lower()   #gets the guess from the user and makes it lowercase
            if (guess in word) and (guessed.count(guess)!=word.count(guess)): #ensures the right letter is guessed the right number of times
                print(guess, "Thats correct", sep="\n")
                guessed.append(guess)   #adds the guessed letter to the guessed list
            else:
                print("_", "You have {} trial(s) left" .format(trials-1), sep="\n")  #this reduces the trials by 1 and informs the user of the trials left 
                trials-=1
        if(len(word)==len(guessed)): 
            return "You won"
        else:
            return "You lost"
print(Hangman("IkeOkoro", 5))

    
