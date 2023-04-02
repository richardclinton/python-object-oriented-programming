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
    
class Snake(Animal):
    def sound(self):
        print("I can hiss")
        
class Dog(Animal):
    def sound(self):
        print("I can bark")
        
class Lion(Animal):
    def sound(self):
        print("I can roar")
        
class Cat(Animal):
    def sound(self):
        print("I can meow")
        
# Our abstratct class has a concrete method sleep() that will be the same for all the child classes.
# So, we do not define it as an abstract method, thus saving us from code repetition. On the other hand, the
# sounds that animals make are all different. For that purpose we define the sound() method as an abstract method.
# We then implement it in all child classes.

cat = Cat()
cat.sleep()
cat.sound()

snake = Snake()
snake.sound()

# If we want to access the sound() function of the base class itself, we can use the object of the child class,
# but we will have to invoke it throught super().
class Rabbit(Animal):
    def sound(self):
        super().sound() 
        print("I can squeak")
        
rabbit =  Rabbit()
rabbit.sound()