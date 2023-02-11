# Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.

value = 'c'
userValue = input("guess a number from a to e")
while (userValue != value):
    print("Incorrect")
    userValue = input("guess a number from a to e")
print("welcome user")
