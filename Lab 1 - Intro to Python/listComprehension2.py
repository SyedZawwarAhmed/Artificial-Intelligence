# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

inputList =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

outputList = []

for i in range(len(inputList)):
    if i != 0 and i != 4 and i != 5:
        outputList.append(inputList[i])

print(outputList)