class Person:
    
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        
        
class Employee(Person):
    
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        
# creation of an object variable or instance
employee = Employee('Rahul', 886012, 200000, 'Intern')
employee.display()
employee.details()
    