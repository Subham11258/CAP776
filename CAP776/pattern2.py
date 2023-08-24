print("Pattern 2")
row=6
for i in range(1,row):
    for j in range(row-1,0,-1):
        if j > i:
            print(" ",end=" ")
        else:
            print(i,end=" ")
    print()
