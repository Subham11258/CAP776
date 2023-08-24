def passwdValidator(passwd):
    if len(passwd) < 8:
        print("***The password should be atleast of length 8***")
        return
    characters = ['@','#','&','^','*','!','~']
    uppercase=0
    special_char=0
    
    if not (ch.isdigit() for ch in passwd):
        print("***The password should contain atleast one digit***")
        return
    for ch in passwd:
        if ch in characters and special_char==0:
            special_char=1
        if ch.isupper() and uppercase==0:
            uppercase=1
                
    if special_char==0:
        print("***The password should contain atleast one special character***")
        return
    if uppercase==0:
        print("***The password should contain atleast one uppercase character***")
        return
    print("Valid Password")
    return
    
passwd = input("Enter your password: ")
passwdValidator(passwd)
