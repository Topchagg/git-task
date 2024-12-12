

class Calc():
    def __init__(self):
        pass

    def divide(self,a,b):
        if b == 0:
            raise Exception("You cannot divide by 0")
        return a/b