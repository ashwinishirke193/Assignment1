n=int(input("Enter the number of maximum starts you want in a row"))
for i in range(0,2*n-1):
    if i <n:
        for j in range(0,i+1):
            print("*",end="")
    else:
        for j in range(2*n-1,i,-1):
            print("*",end="")
    print("")