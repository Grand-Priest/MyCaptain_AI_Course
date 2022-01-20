List1=[]
n=int(input("enter number of elements:"))
for i in range (0,n):
  x= int(input())
  List1.append(x)
print("Input: List=",List1)
for j in List1:
  if j>=0:
    print("Output:",end=" ",j, end=" ")
