# Login with subroutine (definition)

def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "Moi" and password == "R":
      print("Welcome Moi!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
    
print("REPLIT LOGIN SYSTEM")
login()