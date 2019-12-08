def cal():
    global Amount
    Amount = Principal*(1+(Interrest/100)/Interval)**(Year*Interval)

def read():
    global Principal,Interrest,Year,Interval
    Principal= int(input('Enter the Principal: '))
    Interrest= int(input('Enter the Interrest: '))
    Year= int(input('Enter the Year: '))
    Interval= int(input('Enter the Interval: '))
    
def Print():
    print('Principal:',Principal)
    print('Interest:',Interrest,'%')
    print('Year:',Year)
    print('Time per year:',Interval)
    print('%.0f'% Amount)

def main():
    read()
    cal()
    Print()

main()