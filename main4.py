n=int(input())
for i in range(n):
  for j in range(n):
    if i==n-1 or j==0 or i==j or i==0 or j==n-i-1 or j==n-1:
      print("*",end=" ")
    else :
      print(" ",end=" ")
  print()
