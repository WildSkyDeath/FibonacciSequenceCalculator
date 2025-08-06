print ("Welcome to Fibonacci Sequence (Upto 100 only)")
try:
    nterms = int(input("How many sequence do you want to get?: "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    elif nterms <=100:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    else:
        print ("\n")
        print("Sorry this Fibonacci Sequence serves upto 100 sequence only")
        print ("Thank you for using my program")
except ValueError:
    print("Invalid input please try again")