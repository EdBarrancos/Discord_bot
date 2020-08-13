class Outer():
    def __init__(self):
        print("Outer finished")
        
    def printInner(self):
        print("Outer Print")
        
            
hi = Outer()
print(isinstance(hi, Outer))