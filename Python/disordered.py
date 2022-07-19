#this program reorders the lines and each line of texts in a text file and writes them into another file named disordered
lyrics=open('C:\\Users\\Shizuo\\Documents\\Armstrong 1.txt') #here the text file is opened
lyrics=lyrics.read()                                         #the texts in the file are read and stored in the variable lyrics
disordered_lyrics=""                                         #a variable containing an empty string is created to store the reordered text
for character in lyrics[::-1]:                               #the loops through all the characters in the text backwards
    disordered_lyrics=disordered_lyrics+character            #here each character iss added to the disordered_lyric variable made above
reordered=open("disordered.txt", "x")                        #this creates the specified file and returns an error if it alreay exist
reordered.write(disordered_lyrics)                           #this opens the created file and writes the input parameter into it
reordered.close()                                            #closes the file
