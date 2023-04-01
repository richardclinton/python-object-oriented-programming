# Define Classs
class ClassName:
    # Statement-1
    # .
    # .
    # .
    # Statement-N
    pass
    
# Object definition
class Dog:
    pass

obj = Dog()


# The self
# class methods must have an extra first parameter in the method definition. We do not give a value for this
# parameter when we call the method, Python provide it.
# If we have a method that takes no argument, then we still have to have one argument
# This is similar to `this` pointer in C++ and `this` reference in Java.
# When we call a method of this object as myObject.method(arg1,arg2), this is automatically converted by Python
# into MyClass.method(myObject, arg1, arg2)
    
    