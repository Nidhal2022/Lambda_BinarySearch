class Employee:
    def __init__(self, name, eid, salary):
        self.EmployeeName = name
        self.id = eid
        self.salary = salary
    
    def descripe(self):
        return f"Employee Name: {self.EmployeeName} ,id= {self.id} ,salary= {self.salary} Omani Riyals"
        
    
    def getName(self):
        return self.EmployeeName
    def getid(self):
        return self.id
    def getsalary(self):
        return self.salary