def factor():
  num=int(input("Enter the number of which factors to be calculated :"))

  for x in range(1,num+1):
    if(num%x==0):
      print(x)
  
factor() 
