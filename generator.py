
def myfun():
  n=2
  print("value of n is ::%d"%(n))
  yield n

  n=n+1
  print("value of n after increment is :: %d"%(n))
  yield n
 
  n=n-1
  print("value of n after decrement :: %d"%(n))
  yield n


a=myfun()
next(a)
next(a)
next(a)
