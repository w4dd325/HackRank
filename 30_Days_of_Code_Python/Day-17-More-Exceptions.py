class Calculator:
    
    def power (self,n,p):
        # The self parameter is a reference to the current instance of the class
        # and is used to access variables that belongs to the class.
        self.n = n
        self.p = p
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p
        
        
