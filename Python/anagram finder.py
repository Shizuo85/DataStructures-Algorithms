def anagram_finder(word_list):
    #this function takes in a list of words as argument and and returns a list containing anagrams of the list in sublists
    if type(word_list)!=list: #first the argument is checked to ensure the right data type
        return "invalid argument type"
    else:
        anagram_list=[]                     #an empty list where the sublists will be stored 
        anagrams=[]                         #an empty list where all anagrams will be stored
        if(len(word_list)<2):               #when the list contains less than two elements, it is returned unchanged
            return [word_list]
        else:
            for i in range(len(word_list)): #here each index in the list is looped through to check if the index element has any anagram in the list
                if type(word_list[i])!=str: #when a none integer word is found in the list, it is skipped
                    print("Element",word_list[i],"was skipped", sep=" ")
                    continue
                if word_list[i] in anagrams:#when the index element is found in the anagram list(explained above), it is skipped
                    continue
                else:
                    anagram_set=[word_list[i]] #this list will contain all anagrams in the same group per iteration.
                    for k in range(i+1, len(word_list)): #loops through all indexes ahead of i
                        count=0                          #this is used to check the number of similar letters words have in commmon
                        if word_list[k] in anagrams:     #when the index element is found in the anagram list(explained above), it is skipped
                            continue
                        elif len(word_list[i])!=len(word_list[k]): #when the number of letters in index i and k are different, k is skipped
                            continue
                        else:
                            for m in range(len(word_list[k])): #this loops through all the letters in k
                                if word_list[i][m].lower() in word_list[k].lower(): #this compares each letter in index i and k(in lowercase) together
                                    count+=1                            #the count increases by 1 for each letter they have in common
                                else:                                   #once theres a difference in letter, index k is skipped
                                    continue
                                if(count==len(word_list[k])):           #when the count equals the length of word k, words i and k are anagrams
                                    anagrams.append(word_list[i])       #adds the word i to the anagrams list
                                    anagrams.append(word_list[k])       #adds the word k to the anagrams list
                                    anagram_set.append(word_list[i])    #adds the word i to the anagram_set list
                                    anagram_set.append(word_list[k])    #adds the word k to the anagram_set list
                anagram_list.append(list(set(anagram_set)))
                #at the end of the for loop, the anagram_set is added to the anagrem_list (using the set method to remove repetitions) 
            return anagram_list #finally, the complete anagram_list is returned
print(anagram_finder(["hied","boOk", "koob", "kobo",[], "kboo", "hide", "dihe", "bkoo","tea"]))

                               
        
