# Polymorphism means having many forms. For example, we need to determine if the given
# species of birds fly or not, using polymorphism we can do this using a single function.

class Bird:
    
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")
        
        
class Sparrow(Bird):
    def flight(self):
        print("sparrows can fly.")
        
class Ostrich(Bird):
    
    def flight(self):
        print("ostriches cannot fly.")
        
        
    