# It describes the idea of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly and can prevent accidental modification
# of data. To prevent accidental change, an object's variable can only be changed by an object's method. Those
# types of variables are known as private variables.

class Base:
    
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
        
        
class Derived(Base):
    
    def __init__(self):
        super().__init__()
        print("Calling private member of the of base class.")
        print(self.__c)
        
        
base = Base()
print(base.a)