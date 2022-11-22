def leap_year(year):
    return True if(year%4==0 and year%100!=0) or year%400==0 else False
def Day(year,month):
    all_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year):
        all_month[1]=29
    return all_month[month-1]

def first_day(year):
    where=0
    for i in range(1,year+1):
        if leap_year(i):
            where+=1

        where +=1
    return where%7
        

def Calendar(year,month):
    print('SU MO TU WE TH FR SA')
    firstday=first_day(year)-1
    for i in range(1,month):
        firstday+=Day(year,i)
    firstday%=7
    for d in range(firstday+1):
        print('   ',end='')
    d=firstday+2
    for days in range(1,Day(year,month)+1):
        print("{:2d}".format(days),end=' ')
        if d%7==0 and d!=0:
            print('')
        d+=1
    print('')



year,month=map(int,input().split())
Calendar(year,month)