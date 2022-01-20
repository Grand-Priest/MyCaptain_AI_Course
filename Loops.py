terms=int(input("how many terms required"))

n0,n1=0,1
i=0

if terms<=0:
    print("Please enter positive integer")
elif terms=1:
    print("Fibonacci numbers are", terms,":")
    print(n0)
else:
    print("Fibonacci numbers are:)
    while i<terms:
        print(n0)
        nth=n0+n1
        n0=n1
        n1=nth
        i+=1
