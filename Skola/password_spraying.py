# Dictionary över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234"
}

# En lista över vanligt använda lösenord
password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]


with open("password_spraying_result.txt", "w") as f:
    for user, correct_password in user_credentials.items():
        for password in password_list:
            if password == correct_password:
                f.write(f"{user}: {password} -> success\n")
                print(f"{user}: {password} -> success")
            else:
                f.write(f"{user}: {password} -> failed\n")
                print(f"{user}: {password} -> failed")
