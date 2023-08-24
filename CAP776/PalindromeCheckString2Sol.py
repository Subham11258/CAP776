String1 = input("Enter the string to be checked: ")
n = len(String1)

half = String1[:n//2]
m = 0
for i in range(n-1,n//2-1,-1):
    if String1[i] == half[m]:
        m = m+1
    else:
        print("The string is not palindrome")
        break
if m == len(half):
    print("The string is a palindrome")
    
    
