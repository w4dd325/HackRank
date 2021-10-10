

class Student(Person):
    #   Class Constructor 
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, testScores):
        # The Python super() method lets you access methods from a parent class from within a child class.
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores
    
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    # Write your function here
    def calculate(self):
        total = 0
        for testScore in self.testScores:
            total += testScore
        avg = total / len(self.testScores)
        if 90 <= avg <= 100:
            return 'O'
        elif 80 <= avg < 90:
            return 'E'
        elif 70 <= avg < 80:
            return 'A'
        elif 55 <= avg < 70:
            return 'P'
        elif 40 <= avg < 55:
            return 'D'
        elif avg < 39:
            return 'T'
    
