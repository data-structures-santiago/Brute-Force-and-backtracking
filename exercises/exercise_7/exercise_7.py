def password( n,current_password, passwords=[],last_char=""):
    if(len(current_password) == n):
        passwords.append(current_password)
        return
    
    for i in "01":
        if(current_password[-1]=="1"):
            password(n,current_password+i,passwords)
        password(n,current_password+i,passwords)


