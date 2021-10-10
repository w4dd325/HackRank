if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # copy arr into an empty set called new_lsit
    new_list = set(arr)
    # remove the max value from the new data set
    new_list.remove(max(new_list))
    # print the new max value
    print(max(new_list))
