n=int(input(":"))
notes=[1, 2, 5, 10, 20, 50, 100, 500]
notes.reverse()
i=0
while(n):
    b=notes[i]
    if n>=b:
        n=n-b
        print(b)
        if n>=b:
            i=0
    else:
        i+=1

    
