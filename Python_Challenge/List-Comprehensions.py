if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
listijk = [] # Declare an empty list.
for i in range(x + 1): # loop range i (+ 1 to loop all numbers, range starts at 0)
    for j in range (y + 1): # loop range j
        for k in range (z + 1): # loop range k
            if i + j + k != n: # if ijk do not equal n
                listijk.append([i,j,k]) # then append ijk to the empty list
print(listijk) # print list
