a=input()
b=input()
i,j,c=0,0,""
while True:
    if i==len(a):
        break
    if ord(a[i])<=ord(b[j]):
       c=c+b[j]
       i+=1
       j+=1
       if c=="".join(b):
           print("YES")
    else:
        print("NO")
        break
       
       
