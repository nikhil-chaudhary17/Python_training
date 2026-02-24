# Read username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == "admin" and password == "1234":
    print("Login Successful")

elif username == "admin":
    print("Incorrect Password")
    
else:
    print("Invalid Username or Password")