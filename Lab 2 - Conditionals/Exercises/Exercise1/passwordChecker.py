password =  "abc$123"
inputPassword = input("What is the password? ").lower()

if password == inputPassword:
    print("Welcome")
else:
    print("I don't know you.")
