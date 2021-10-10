#Call function with "size" set to "n"
def print_rangoli(size):
        
    # Set myStr as alphabet and slice from 0 to value of "size"
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        
        #Get the absolute value of i
        x = abs(i)
        
        #we can use a stride of -1 (the 3rd value in the []
        #to print the original string in reverse order
        
        #example; 
        #myStr[x:size] ==  bcde
        #myStr[size:x:-1] ======  edc
        line = myStr[size:x:-1]+myStr[x:size]
        
        # "--"*x  ==  fill characters
        # '-'.join(line)  ==  Joins all characters from "line" with a hyphen
        print ("--" * x + '-'.join(line) + "--" * x)

