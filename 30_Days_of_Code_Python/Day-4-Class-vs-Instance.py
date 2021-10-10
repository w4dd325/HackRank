class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
            
    def amIOld(self):
        # Do some computations here and print out the correct statement to the console  
        if 0 <= self.age <= 12 :
            print("You are young.")
        elif 13 <= self.age <= 17:
            print("You are a teenager.")
        else:
            print("You are old.")
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        
