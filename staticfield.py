class Student:
    stream="ECE" #static or class variable
    def __init__(self,name,rollno):
        self.name=name
        self.roll=rollno

s1=Student("John",1)
s2=Student("Bill",2)

print("Loading Student1 ...")
print("Department: ",s1.stream)
print("Name: ",s1.name)
print("Roll No. ",s1.roll)

print("Loading Student2 ...")
print("Department: ",s2.stream)
print("Name: ",s2.name)
print("Roll No. ",s2.roll)