import random

wordle = ["bulky", "house", "trail", "watch", "black", "aired", "ounce", "squad", "peach", "nymph", "pivot", "quote", "error", "ivory", "crept", "kajin", "jumpy", "drank", "fails", "gummy"] 
word=wordle[random.randint(0, 19)] #a random word is selected from a list of 20 words

trial=0
guess= ""
while trial<6 and guess!=word:
  guess= input("Enter guess: ").lower()
  result=""  
  
  if guess.isalpha()!= True or len(guess)!=5: #this checks for proper input
    print("Enter a five letter word")
    continue

  trial+=1
    
  for k in range(5):
    if word[k]==guess[k]: result+="√"
      
    elif guess[k] in word:
      if guess.count(guess[k])<=word.count(guess[k]): result+="+"
      else: #this checks for repeated letters
        lst1 = [x for x in range(5) if guess[x]==guess[k]] #list of indexes of a letter in the guess
        lst2 = [y for y in range(5) if word[y]==guess[k] and y not in lst1 ]#list of indexes of a letter in the word that doesn't align in guess
        if k in lst1[:len(lst2)]: result+="+"
        else: result+="*"
          
    else: result+="*"
      
  print(result)

if word!=guess: print("The word is", word)
