def fibo():
  a,b=0,1
  temp=0
  print(temp)
  while temp!=6:
    sum=a+b
    a,b=b,sum
    print(a)
    temp+=1
 
fibo()

