String1 = input("Enter string 1:")
String2 = input("Enter string 2:")
if len(String1)!=len(String2):
    print("The length of the strings must be same")
else:
    s1 = String1.lower()
    s2 = String2.lower()
    listA = []
    match = 0
    for ch in s1:
        for ch1 in s2:
            if ch == ch1 and ch1 not in listA:
                match+=1
                listA.append(ch1)
                break
        
    if match == len(s1):
        print("The Strings are anagram of each other")
    else:
        print("The Strings are not anagram of each other")
