z=int(input())
n=list(map(int,input().split()))
if len(n)==z:
    i=c=0
    j=1
    a=[]
    while(True):
        if i==len(n)-1:
            break
        if n[i]>=n[j]:
            c+=1
            if j<=len(n):
                j=j+1
            if c==len(n)-i:
                    a.append(n[i])
            if j==len(n):
                i=i+1
                j=i+1
                c=1
        else:
            i=i+1
            j=i+1
            c=1
    a.append(n[-1])
    for k in a:
        print(k,end=" ")
    
    
            
        
