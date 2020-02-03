n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=j=0
if len(a) and len(b)==n:
    while True:
        if a[j]!=b[j]:
            a.append(a[0])
            a.remove(a[0])
            c+=1
        else:
            if a[j]==b[j]:
                a.remove(a[j])
                b.remove(b[j])
                c+=1
        if (len(a) and len(b))==0:
            break
print(c)
