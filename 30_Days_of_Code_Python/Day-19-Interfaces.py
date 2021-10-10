class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        val = 0
        for i in range(1,n+1):
            # Modulus operator; gives the remainder of the left value divided by the right value
            if(n % i == 0):
                val += i
        return val
