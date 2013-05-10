__author__ = 'JohnLiu'

class Employee:
    "This is a bass class for all employees"
    employee_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.employee_count = self.employee_count + 1
        print "%d" % self.employee_count

    def display_count(self):
        print "current employee counnt : %d" % self.employee_count

    def display_employee(self):
        print "employee info \n name : %s \t salary : %s" %( self.name, self.salary)

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, ' is destroyed'

emp_1 = Employee("John Nash", 20000)
emp_2 = Employee("Anna", 9000)
emp_1.display_employee()
emp_2.display_employee()
emp_1.age = 19
# hasattr(emp_1, 'age')    # Returns true if 'age' attribute exists
# getattr(emp_1, 'age')    # Returns value of 'age' attribute
# setattr(emp_1, 'age', 8) # Set attribute 'age' at 8
# delattr(emp_1, 'age')    # Delete attribute 'age'
# del emp_1.age
print 'employee age : ', emp_1.age, hasattr(emp_1, 'age') ,getattr(emp_1, 'age')  ,setattr(emp_1, 'age', 8)
#call __del__ function
del emp_1
# __dict__ : Dictionary containing the class's namespace.
# __doc__ : Class documentation string, or None if undefined.
# __name__: Class name.
# __module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
# __bases__ : A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__


