if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    #save list a tuple
    t = tuple(integer_list)
    #print hash of t
    print hash(t)