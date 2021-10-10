def mutate_string(string, position, character):
    #Join 3 sub strings
    #The characters before the position of character to be replaced
    #The character to be replaced
    #And, the characters after the +1 position
    return string[:position] + character + string[position + 1:]

