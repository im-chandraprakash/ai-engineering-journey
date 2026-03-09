# class Car : 
#     brand = ""
#     model = ""
#     price = 0

#     def display(self) :
#         print("Car Brand Name : " , self.brand)
#         print("Car Model Name : " , self.model)
#         print("Car Price Name : " , self.price)


# c1 = Car()
# c1.brand = "Suzuki"
# c1.model = "Alto"
# c1.price = 100000.00

# c1.display()


class Employee : 
    name = ""
    salary = 0
    departmenet = ""

    def __init__(self, name , salary, department) : 
        self.name = name
        self.salary = salary
        self.department = department
    
    def display(self) : 
        print("Name of employee : " , self.name)
        print("Salary of employee : " , self.salary)
        print("Department of employee : " , self.department)

e1 = Employee("Cp" , 263212 , "Development")
e1.display()