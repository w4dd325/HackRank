if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
# SOLUTION 1
# Search the "student_marks" list for "query_name" and when there is a match
# save the values into "query_score"

# Example:
# student_marks =  {'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
# query_name =  Malika
# query_scores =  [52.0, 56.0, 60.0]
query_scores = student_marks[query_name]

# Sum the scores in the list: total_scores
total_scores = sum(query_scores)

# Divide the total scores by number of people to get average
# And format the float to 2 decimal places
avg = "{:.2f}".format(total_scores/3)

# Print the mean of the scores, correct to two decimals
print(avg)



# SOLUTION 2
#print("{:.2f}".format(sum(student_marks[query_name])/3))
