## Skapa och spara användarnamn och lösenord.
## Senare att göra: Spara varje användare + lösenord i filen User_login.txt

print("Create a username and password - program")    
username = input(f"Choose your username: ")
password = input(f"Choose your password: ")
credentials = (username, password)

print("Your username is: " + username)
print("Your password is: " + password)


print("Log in to your account")
while True:
    check_username = input("Enter your username:")
    if check_username == username:
        break
    else:
        print("Yout entered the wrong username, try again")
while True:
    check_password = input("Enter your password:")
    if check_password == password:
        break
    else:
        print("Yout entered the wrong password, try again")
print("SUCCESS, you were logged in!")

