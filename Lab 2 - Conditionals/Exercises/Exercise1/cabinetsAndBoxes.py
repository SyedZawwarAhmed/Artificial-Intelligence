height = float(input("Enter height:- "))
width = float(input("Enter width:- "))
depth = float(input("Enter depth:- "))

volume = height * width * depth

volumeRanges = {
    "Extra Small": {
        "lower": 1,
        "upper": 10
    },
    "Small": {
        "lower": 11,
        "upper": 25
    },
    "Medium": {
        "lower": 26,
        "upper": 75
    },
    "Large": {
        "lower": 76,
        "upper": 100
    },
    "Extra Large": {
        "lower": 101,
        "upper": 250
    },
    "Extra-Extra Large": {
        "lower": 251,
        "upper": None # this is because, there is no upper limit in this case
    },
}

print(f'The volume is {volume}.')

for key, value in volumeRanges.items():
    if value['upper'] == None:
        print(key)
    elif volume >= value['lower'] and volume <= value['upper']:
        print(key)
        break
        
