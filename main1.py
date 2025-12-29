x="madam"
l=0
r=len(x)-1
while l<r:
  if x[l]==x[r]:
   l+=1
   r-=1
   print("palindrome")
  else:
    print("not a palindrome")
