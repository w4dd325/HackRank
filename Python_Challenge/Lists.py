if __name__ == '__main__':
    N = int(input())
    
    # create a new blank list
    myList = []
    
    for _ in range(N):  #loop through the range
        s = input().split()  #split up the input
        cmd = s[0]  #example:  insert
        args = s[1:]  #example:  ['1', '10']
        
        #if the command is not "print"
        if cmd !="print":  
            #re-write the command with new args
            cmd += "("+ ",".join(args) +")"  
            #evaluate cmd and update myList. example: [5, 10]
            eval("myList."+cmd)  
        else:
            #otherwise, just print the list
            print(myList)
