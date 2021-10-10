def merge_the_tools(string, k):
    
    #for each in range 0 to string length and increment by k
    for i in range(0,len(string), k):
        
        #slice string upto k characters
        line = string[i:i+k]
        seen = set()
        for i in line:
            #only print if we haven't already seen this character
            if i not in seen:
                print(i,end="")
                #add to seen set so no used in future iterations
                seen.add(i)
        #empty print to get the default end="\n" back
        print()

