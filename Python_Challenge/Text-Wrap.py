def wrap(string, max_width):
    #textwrap.wrap wraps the single paragraph in text (a string) 
    #so every line is at most width characters long. 
    #Returns a list of output lines, without final newlines.
    #https://docs.python.org/3/library/textwrap.html
    #
    #***********************************************************
    #
    #to print the list as required we can join all segments of 
    #the list using \n 
    return "\n".join(textwrap.wrap(string, max_width))
