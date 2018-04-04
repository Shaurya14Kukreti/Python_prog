import math

def armstrong(num):
  f=0
  temp=int(num)
  while temp>0: 
    a=int(temp%10)
    f = f+(a**3)
    temp=temp/10

  print(f)
  if f==num:
     print("number {} is armstrong ::".format(num) )
  else:
     print("number {}  is not armstrong :".format(num))  


a=int(input("enter number to check armstrong or not ::"))
armstrong(a)
