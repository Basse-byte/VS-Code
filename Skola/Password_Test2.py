# Dictionary över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234"
}

# En lista över vanligt använda lösenord
password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]


with open("PW_results2", "w") as pw_list: # Öppnar/skapar en ny txt fil som heter PW_results2 och "w" för att skriva in i filen.
    for user, correct_pw in user_credentials.items(): # För varje user och correct pw i dict user_credentials kollar vi en bokstav/element i taget.
        for password in password_list: # För varje lösenord/string i password_list
            if password == correct_pw:
                pw_list.write(f"{user}: {password} -> success\n") # Skriver i PW_results2 vilken user som matchar med vilket password. och skriver -> success. och byter till ny rad.
                print(f"{user}: {password} -> success") # skriver ut  samma sak i terminalen för visuell bekräftelse.
            else:
                pw_list.write(f"{user}: {password} -> failed\n") # Skriver i dokumentet att försöket misslyckades.
                print(f"{user}: {password} -> failed") # Skriver i terminalen att försöket misslyckades.

