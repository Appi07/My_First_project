#Real Time Example 2

from tkinter import E


class Employee:
    def __init__(self,Name,Occupation,Salary,Experience):
        self.name=Name
        self.occupation=Occupation
        self.salary=Salary
        self.experience=Experience
        
    print("_"*50)
    
    
    def details(self):
        print("Employee[{},{},{},{}]".format(self.name,self.occupation,self.salary,self.experience))
    
    
    print("50"*50)          
        
        
        