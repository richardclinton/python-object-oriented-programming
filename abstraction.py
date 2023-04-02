# It hide unneccessary code details from the user. Also, when we do not want to give out sensitive parts 
# of our code implementation and this is where data abstraction came. Data abstraction in python is archieved
# by through creating abstract classes.

from abc import ABC, abstractmethod

class Animal(ABC):
    
    # concrete method
    def sleep(self):
        print("I am going to sleep in a while")
       
    @abstractmethod 
    def sound(self):
        print("This method is for defining the sound by any animal.")
        pass