getSquare = lambda list : [item ** 2 for item in list]
getCube = lambda list : [item ** 3 for item in list]

list = [1, 2, 3, 4, 5]
print(getSquare(list))
print(getCube(list))