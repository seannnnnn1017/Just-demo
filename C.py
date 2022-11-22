m,n=map(int,input().split(' '))
def Factorial(x):
    ans=1
    for i in range(1,x+1):
        ans*=i
    return ans

def C(m,n):
    top=Factorial(m)
    bottom=Factorial(n)*Factorial(m-n)
    return (top/bottom)
print(C(m,n))