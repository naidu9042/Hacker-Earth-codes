# if n is not prime then print next prime
"""n=int(input("enter number:"))
while(True):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print("prime is",n)
        break
    else:
        n+=1
    
    #print(n)"""



n=int(input("enter number:"))
h=h1=0
c2=0
for k in range(1,n+1):
    if n%k==0:
        c2+=1
if c2==2:
    print("prime")
else:
    while(True):
        c=c1=0
        h=h1=0
        for j in range(1,n):
            for i in range(1,n+2):
                if (n+j)%i==0:
                    c+=1
                    h+=1
                    #print(h)
                if (n-j)%i==0:
                    c1+=1
                    h1+=1
                    #print(h1)
                    
            if c==2 and h<h1 or h==h1:
                print("prime is",n+j)
                break
            elif(c1==2)and h1<h:
                print("prime is",n-j)
                break
        
        break






