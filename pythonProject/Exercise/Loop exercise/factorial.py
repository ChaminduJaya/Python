def fact(n) :
    f=1
    for i in range (1,n+1) :
        f=f*i
    return f
print (fact(4))

def fact2(n):
    if n==0:
        return 1
    return n * fact2(n-1)
print (fact2(4))