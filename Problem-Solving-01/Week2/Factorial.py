def Factorial(N):
    if N > 1 :
        NFactorial = N*Factorial(N-1)
    else :
        NFactorial = 1
    return NFactorial

def main():
    global N
    N = int(input('Enter Number : '))
    Factorial(N)
    print(Factorial(N))
main()
