

class Calc():
    def __init__(self):
        pass

    def divide(self,a,b):
        if b == 0:
            raise Exception("You cannot divide by 0")
        return a/b
    
    def plus(self,a,b):
        return a+b
    
    def multiply(self,a,b):
        return a*b
    
    def minus(self,a,b):
        return a-b