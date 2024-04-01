a=[1,2,3,4,5,4,3,2,1]
rev_a =[]
lenA=len(a)
for i in range(lenA-1,-1,-1):
    rev_a.append(a[i])
if(a==rev_a):
    print ("Palindrome")
else:
    print("Not Palindrome")
