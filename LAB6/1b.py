s="himank,j.o'shi"
c=""
for i in s:
  if i>='a' and i<='z':
    c=c+i
  elif i>='A' and i<='Z':
    c=c+i
  elif i>='0' and i<='9':
    c=c+i
  elif i==' ':
    c=c+i
print(c)