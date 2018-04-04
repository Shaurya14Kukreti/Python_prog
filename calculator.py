def add(x,y):
 return x + y

def sub(x,y):
 return x - y

def mul(x,y):
  return x * y
  

def divide(x,y):
 return x/y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

num = input("enter choice 1/2/3/4  ::")

num1=int(input("enter first value ::"))
num2=int(input("Enter second value ::"))

if num == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif num == '2':
   print(num1,"-",num2,"=", sub(num1,num2))

elif num == '3':
   print(num1,"*",num2,"=", mul(num1,num2))

elif num == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
