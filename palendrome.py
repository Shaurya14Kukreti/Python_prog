def palendrome(num):
 temp=int(num)
 f=0
 while num>0:
  a=int(num%10)
  f= (f*10+a)
  print(f)
  num=int(num/10)

 if f==temp:
  print("number is palendrome  ",temp)
 else:
  print("number is not palendrome ",temp)   
  

palendrome(23)
