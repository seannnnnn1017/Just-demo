def fun(n):
    if n <10:
        return 1
    return 1+fun(n//10)
print(fun(4395))