

# Complete the solve function below.
def solve(s):
    
    #Split the input value on space and save as list
    wordList = s.split(" ")
    
    #Create new list where each word in the list is capitalized
    capitalized_words = [eachWord.capitalize() for eachWord in wordList]
    
    #Rejoin the words with a space and return/output
    return " ".join(capitalized_words)

