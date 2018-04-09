
def reverse(s):
  str = ""
  for i in s:
      str=i+str
     
  return str    



string = "A man, a plan, a canal: Panama" 

st = string.replace(" ", "")
t =st.casefold()

y=''
for x in t:
  if(((x >="a")and(x<="z"))or('0'<=x <='9')):
      y +=x
      
  else:
     continue
 
#print("String after removal of special characters is  ::",y)

if (y==""):
   print("string is empty")
   
str1 = reverse(y)
#print( "String after reverse function is  ::  ",str1)

if(y==str1):
  print("String is palendrome  ")
else:
  print("String s not palendrome")
      
