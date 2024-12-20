# Problem 2
def Collatz(n):
    for i in range(20):
        if n % 2 == 0:
            n = n/2
            print(n)
        else:
            n = n*3 + 1
            print(n)
Collatz(1)