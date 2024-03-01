# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:29:27 2024

This program is designed to create a list of all the perfect words that can be made starting with any letter.

@author: TripleBBB
"""
"""


"""
def isWord(word):
    return 1 if (word in wordList) else 0

"""

"""
def genList(word): #Generates a list of all the 
    temp = [] #temp array 
    
    #If empty, create list
    if word == []: #Yes, I'm wasting a couple of cycles every time to check for this. No, I don't care. It makes the actual code somewhat easier to read.
        for letter in alphabet:
                       temp.append(letter)
        return temp
    
    #If not empty, create a list of every acceptable word that can be made from this word
    for  letter in (alphabet):
        if (isWord(word + letter)):
            temp.append(word + letter)
            #print(word + letter) #DEBUG
    return temp
""""""
  
def listElab(wordList):
    #The function that calls recursively.
    return print(wordList)

if __name__ == "__main__":
    
    #Setup:
    f = open('allWords.txt', 'r')
    wordList = f.readlines()    #I'm re-using some of my code from my boggle project. I made this project when I was a softmore. Is it efficient? No. Is it elegant? No. Does it work? Sometimes.
    for v,x in enumerate(wordList):
        wordList[v] = x[:-1] #Removes the newline from each line, giving us a list of words, the whole words, and nothing but the words.
    wordList[-1] = "ZZZS" #The above for loop strips the "s" from the last word, unfortunately. While I don't predict "ZZZS" being a perfect word, it's worth an attempt.
    f.close()
    #Create an initial array for every letter of the alphabet.
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #We're hard-coding every individual letter to fit in these words, as not every individual letter is technically a word in scrabble standards.
    
    #Let's have a list of all of these individual lists. Sounds goofy, is goofy, but should work.
    mainList = genList([])
    
    #Setup complete, let's get into the actual iterative process:
    f = open("perfect-words-temp.txt", 'w')
    try:
        for item in mainList:
            f.write(item + "\n")
            mainList.extend(genList(item))
        #Glad that's done!
        f.close()
    except:
       print("You stopped me too soon!")
       f.close()