class Student:
 
    __rollno = 0
    name = ""
 
    def __init__(self):
        self.__rollno = 200
        self.name = "shaurya"
 
    def print(self):
        print ("roll no of given student is  "+str(self.__rollno))

 
stud = Student()
stud.print()
stud.rollno = 10  # will not change variable because its private
stud.print()
