def print_formatted(number):
    space = len(str(bin(number))) 
    for i in range(1, number + 1): 
        f = str(i) 
        o = str(oct(i)[2:]) 
        h = str(hex(i)[2:]).upper() 
        b = str(bin(i)[2:]) 
        #[2:] is slice notation
        #https://stackoverflow.com/questions/509211/understanding-slice-notation
        
        formatted_f = ((" " * (space - len(str(f)) - 2)) + f) 
        formatted_o = ((" " * (space - len(str(o)) - 2)) + o) 
        formatted_h = ((" " * (space - len(str(h)) - 2)) + h) 
        formatted_b = ((" " * (space - len(str(b)) - 2)) + b) 
        
        print(formatted_f + " " + formatted_o + " " + formatted_h + " " + formatted_b)

