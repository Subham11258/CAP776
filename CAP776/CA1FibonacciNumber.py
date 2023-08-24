n = int(input("Enter the number:"))
arr = [0,1]
j=2
while j!=n:
    arr.append(arr[j-1]+arr[j-2])
    j+=1
print("Fibonacci array is:",arr)
arr.reverse()
print(" reversed of the Fibonacci array is:",arr)

