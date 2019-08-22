

#Python Dictionary Program
#Olowonyo Olawale
#twitter @wale_io 

import json
from difflib import get_close_matches
#difflib is a library which helps find matching or closely matching words from a given data set

sourceData = json.load(open("data.json"))
#This opens the data.json file and stores it to the variable sourceData 


def query(w):
    w = w.lower()
    if w in sourceData:
        print("Heres the Definition of {} below \n".format(w))
        print(sourceData[w]) 
        # return sourceData[w]
        print("\n")
    #if the word, which is the "key" is in the source data file, it returns the "value" pair

    elif len(get_close_matches(w, sourceData.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, sourceData.keys())[0])
        if yn == "Y":
            return sourceData[get_close_matches(w, sourceData.keys())[0]]
            #Checks for close matches with the library 


        elif yn == "N":
            return "This word does not exist in the Dictionary. Please try again."
        else:
            return "Wrong Input."
    else:
        return "The word doesn't exist. Please double check it."
        

 
rt = True
# This is a condition for while loop, for the dictionary to keep asking the user for input.

while rt ==True:
    print('\n The Best CLI Dictionary on the Planet,------Press "N" to quit this Dictionary \n')

    word = input("Input your word below here my Good friend :\n ")
    if word == "N":

        rt == False 
        break
    else:
        query(word) 
