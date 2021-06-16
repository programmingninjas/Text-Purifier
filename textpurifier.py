from fuzzywuzzy import fuzz

def quick_censor(data):

    with open('badwords1.txt','r') as file:
    
        words = file.read().split('\n')

        for word1 in words:

            for word2 in data.split():

                if fuzz.ratio(word1,word2)>90:  #Adjust this ratio according to yourself

                    data = data.replace(word2,'*'*len(word2))
        
        return data

def deep_censor(data):

    data = quick_censor(data)

    with open('badwords2.txt','r') as file:   #badwords2 contains abusive words with spaces because to handle this issue we will need to use NLTK library of python which is used for natural language processing and things will be complicated.
                                              #If you have a simple solution for it DM me on insta @programmingninjas. 
        words = file.read().split('\n')

        for word in words:

            if data.find(word)!= -1:

                data = data.replace(word,'*'*len(word))

    return data


    
