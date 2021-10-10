_ = set(input().split()) # input line 1 - number of students / English newspaper
a = set(input().split()) # input line 2 - space separated roll numbers / English students
_ = set(input().split()) # input line 3 - number of students / French newspaper
b = set(input().split()) # input line 4 - space separated roll numbers / French students
# _ is used to store the unneeded inputs

# For Debugging
# print("a = ", a) # Check what is set in variable a
# print("b = ", b) # Check what is set in variable b
# print(a.intersection(b)) # Outputs the dulplicates
# .intersection returns all duplicate elements from both sets, as a new set

print(len(a.intersection(b))) # Use 'len' to count duplicates
# len returns the number of items in a container
