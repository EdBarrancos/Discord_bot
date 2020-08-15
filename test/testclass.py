from .testforthur.testcrazy import crazy
class Outer():
    def __init__(self):
        crazy()
        
    def printInner(self):
        print("Outer Print")
        
            
hi = Outer()
print(isinstance(hi, Outer))