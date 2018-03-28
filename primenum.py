
a=input("enter number to check whether it is prime number or not  ::")
flag=0
b=a-1
for x in range(2,b):
  if (a%x)==0:
    print (a,"number is not prime number")
    flag=1
    break
  else:
    flag=0

if(flag==0):
  print (a,"is a prime number")


