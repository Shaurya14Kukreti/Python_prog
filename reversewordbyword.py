#function to split the entered string whenever " "space encounters 
#reverse the string 
def reverse(input):
  str = input.split(" ")
  str = str[::-1]
   
   

  return str

#program starts here
#take input from user and call reverse function
input = input("enter string to reverse word by word ::") 
print(reverse(input)) 
