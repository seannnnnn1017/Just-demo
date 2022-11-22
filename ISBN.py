num=input().split(' ')
def ADD(num):
    first_add=[num[0]]
    for i in range(1,len(num)):
        first_add.append(num[i]+first_add[i-1])
    return first_add
def ISBN(num):
    for index,number in enumerate(num):
        if number =='X':
            num[index]=10
        else:
            num[index]=int(number)
    last=ADD(ADD(num))
    return 'YES' if last[len(num)-1]%11==0 else "NO"
print(ISBN(num))