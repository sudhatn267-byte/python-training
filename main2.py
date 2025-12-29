def check(x):
    l=0
    r=len(x)-1
    while l<r:
        if x[l]!=x[r]:
          return ("not a palindrome")
        else:
            l+=1
            r-=1
            return ("palindrome")
        x="madam"
        print(check(x))
