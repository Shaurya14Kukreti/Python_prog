def subarray(li1):
    sublist = []
    
    for i in range((len(li1)+1)):
        for j in range(i + 1, (len(li1)+1)):
            sub = li1[i:j]
            sublist.append(sub)
           # print(sublist)
             
          
    return sublist
 
l1 =[2,1,-3,4,-1,2,1,-5,4]
f=0
str =subarray(l1)
#print(str)

for i in range(len(str)):
    s =sum(str[i])
 
   
    if s>=f:
      f=s
      print("the subarray {} has max sum ::{}".format(str[i],s))
    else : pass
		 
   

