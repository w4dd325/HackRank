if __name__ == '__main__':
    
    # Create empty list
    myList = []
    second_lowest_names = []
    # Create empty set
    scores = set()
    
    for _ in range(int(input())):
        # First input is the number of people
        # We use this figure as the range max 
        # and save each input into the name and score variables
        name = input()
        score = float(input())
        # Create the nested list by adding name and score into each row
        myList.append([name, score])
        # Add each score the our set (sets are itterable)
        scores.add(score)
        
    # Sort the scores and pick [1] aka second array entry and save to variable
    second_lowest = sorted(scores)[1]

    # Move through the list and add "name" is "second_lowest" matches "score" 
    for name, score in myList:
        if score == second_lowest:
            # Add all second lowest names to our other list
            second_lowest_names.append(name)

    # Sort the list and display each name on a new line
    for name in sorted(second_lowest_names):
        print(name, end='\n')
