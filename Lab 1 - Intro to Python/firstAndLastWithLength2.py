inputList = ['abc', 'xyz', 'aba', '1221', 'addda', 'racecar']

count = 0
for string in inputList:
    if len(string) >= 2 and string[0] == string[-1]: 
        count += 1

print(count)