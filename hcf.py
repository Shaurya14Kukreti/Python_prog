def cal_hcf():
  num1=int(input("enter 1st number  ::"))
  num2=int(input("enter second number ::"))
  
  if num1>num2:
    small = num2
  else:
    small = num1
  
  for x in range(1,small+1):
    if(num1%x==0) and (num2%x==0):
      hcf = x
   
  return hcf 

print ("Hcf of the two numbers  is ", cal_hcf())
