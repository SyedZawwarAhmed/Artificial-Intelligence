a = int(input("Enter a number:- "))
b = int(input("Enter a number:- "))
c = int(input("Enter a number:- "))
d = int(input("Enter a number:- "))

arr = [a, b, c, d]

print(f'Before swapping:- a = {a}, b = {b}, c = {c}, d = {d}')

[d, c, b, a] = arr

print(f'After swapping:- a = {a}, b = {b}, c = {c}, d = {d}')
