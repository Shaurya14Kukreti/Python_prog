#function to remove all unwanted characters 
def fun(line):
  empty =""
 # print(line)
  for x in line:
    if(((x >="a")and(x<="z"))or('0'<=x <='9')or(x>="A")and(x<="Z")):
        empty +=x
      
    else:
      continue 
  
  
  return empty


#program starts Here
#Read a file line by line using readline() till we get  "" or end of text 
f1 = open("read" ,"r")
line = f1.readline()
while line != "":

# call fun function to check and remove all spaces and special characters   
    str = fun(line)
#reverse the string  
    string = str[::-1]
  #  print(str)
   # print(string)
 
#check if the original string is equals to new reversed string
    if(str.casefold()==string.casefold()):
      print("String is palendrome" , str)
    else:
      print("string is not palendrome",str)
     
    line = f1.readline()



  

