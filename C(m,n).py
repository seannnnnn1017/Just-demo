
def Factorial(x):
    ans=1
    for i in range(x):
        ans*=i
    return ans

def C(m,n):
    top=Factorial(m)
    bottom=Factorial(m)*Factorial(m-n)
    return top/bottom
print(C(int(input()),int(input())))