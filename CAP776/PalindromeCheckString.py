String1 = input("Enter the string to be checked: ")
reversedStr = String1[::-1]
if String1 == reversedStr:
    print("The string is a palindrome string")
else:
    print("The string is not a palindrome string")
