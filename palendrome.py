# function to reverse the string
def reverse(s):
  str = ""
  for i in s:
      str=i+str
     
  return str    


#starting of program take "A man, a plan, a canal: Panama"  as input 
string = "A man, a plan, a canal: Panama" 
y=''    # empty string

#check for string if it contains characters other than the defined below range ,if yes skip the character  
for x in string:
  if(((x >="a")and(x<="z"))or('0'<=x <='9')or(x>="A")and (x<="Z")):
      y +=x
      
  else:
     continue
      
 # After checking the string  becames (without " " and special characters ): 
print("String after removal of special characters is  ::",y)

# check if string becames empty or is empty after for loop  
if (y==""):
   print("string is empty")
    
#call reverse function    
str1 = reverse(y)
print( "String after reverse function is  ::  ",str1)

#put condition to check whether both strings y and str are equal or not:
if(y.casefold() ==str1.casefold()):
  print("String is palendrome  ")
else:
  print("String s not palendrome")
      
