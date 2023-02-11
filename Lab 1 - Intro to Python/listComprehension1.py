# Write a list comprehension which, from a list, generates a lowercased version of each string that has length greater than five.

inputList =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
outputList = [string for string in inputList if len(string) > 5]

print(outputList)