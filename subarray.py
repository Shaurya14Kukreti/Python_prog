#function subarray : it will create all possible continuous subarrays and return it to str .
#use print to see possible combinations
def subarray(li1):
    sublist = []
    
    for i in range((len(li1)+1)):
        for j in range(i + 1, (len(li1)+1)):
            sub = li1[i:j]
            sublist.append(sub)
           # print(sublist)
             
          
    return sublist
#Starting of program ,take a sample list
l1 =[2,1,-3,4,-1,2,1,-5,4]
f=0
#call subarray() with l1 as argument 
str =subarray(l1)
#print(str)

# iterating each list in str to calculate sum
for i in range(len(str)):
    s =sum(str[i])
 
#  compare and print each sum till we found the greatest sun and its corresponding subarray   
    if s>=f:
      f=s
      print("the subarray {} has max sum ::{}".format(str[i],s))
    else : pass
		 
   

