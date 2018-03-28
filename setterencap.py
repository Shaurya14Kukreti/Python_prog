class Student:
 
    __rollno = 0
    name = ""
 
    def __init__(self):
        self.__rollno = 200
        self.name = "shaurya"
 
    def print(self):
        print ("roll no of given student is  "+str(self.__rollno))

    def setrollno(self,value):
        self.__rollno = value

 
stud = Student()
stud.print()
stud.setrollno(10) 
stud.print()
