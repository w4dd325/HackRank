class Solution:
    
    # 1. Two instance variables: one for your stack, and one for your queue.
    def __init__(self):
        self.stack = []
        self.queue = []

    # 2. A void pushCharacter(char ch) method that pushes a character onto a stack.
    def pushCharacter(self, char):
        self.stack.append(char)    
    
    # 3. A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
    def enqueueCharacter(self, char):
        self.queue.append(char)
        
    # 4. A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
    def popCharacter(self):
        # The argument passed to the method is optional. 
        # If not passed, the default index -1 is passed as an argument 
        # (index of the last item).
        # https://www.programiz.com/python-programming/methods/list/pop
        return self.stack.pop()

    # 5. A char dequeueCharacter() method that dequeues and returns the first character in the queue instance variable.
    def dequeueCharacter(self):
        # Set char as first character from list
        char = self.queue[0]
        # Truncate your list from the first element.
        self.queue = self.queue[1:]
        return char
        
