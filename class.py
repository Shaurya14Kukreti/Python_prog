class Members:
    add = 0

    def __init__(self, name):
        
        self.name = name
        print("name of the family member is ".format(self.name))

       
        Members.add+= 1

    def leave(self):
        print ("member leaves ::".format(self.name))

        Members.add -= 1

        if Members.add == 0:
            print("this is the last member of group ".format(self.name))
        else:
            print("there are still some left :: %d.".format(
             Members.add))

    def say_hi(self):
        
        print("Greetings, my name is .".format(self.name))

    
    def how_many_left(self):
       
        print("We have left with : .".format(self.add))


droid1 = Members("shaurya")
droid1.say_hi()
droid1.how_many_left()

droid2 = Members("satyam")
droid2.say_hi()
droid2.how_many_left()





