class Student():
    def __init__ (self, marks):
        self.marks = marks

    def __lt__(self,other):
        if self.marks < other.marks:
            return "obj1 is less than obj2"
        else:
            return "obj1 is not less than obj2"
        
    def __eq__(self,other):
        if self.marks == other.marks:
            return "obj1 is equal to obj2"
        else:
            return "obj1 is not equal to obj2"

obj1 = Student(3)
obj2 = Student(4)
print(obj1 < obj2)
print(obj1 == obj2)