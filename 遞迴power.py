def powerA(a,n):
    if n==1:return a
    return a*powerA(a,n-1)

def powerB(a,n):
    if n==1:return a
    if n%2==0:return powerB(a,n/2)**2
    return a*powerA(a,n-1)
print(powerB(2,3))