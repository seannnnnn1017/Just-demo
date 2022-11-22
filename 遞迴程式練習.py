
def f( n: int) -> int:
    if n==1:
        return n+1
    else:
        return f(n-1)+f(abs(n//2)) 
print(f(12))
