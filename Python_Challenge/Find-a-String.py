def count_substring(string, sub_string):
    #Set count to 0
    count = 0
    #Search for initial substrings to set i
    i = string.find(sub_string)
    
    #find() return -1 if substring is not present in given string, so use i != -1
    while i != -1:
        #Count how many occurrences
        count += 1
        #Search for subsequent substrings
        i = string.find(sub_string, i+1)
    return count

