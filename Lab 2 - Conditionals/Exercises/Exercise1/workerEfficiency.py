timeTakenByTheWorker = input("Enter the time taken by the workers in the format HH:MM:SS:- ")

time = timeTakenByTheWorker.split(":")
time = [int(item) for item in time]
timeTakenByTheWorkerInHours = time[0] + time[1] / 60  + time[1] / 3600

efficieny = {
    "Highly Efficient": {
        "lower": 2,
        "upper": 3
    },
    "Improve Speed": {
        "lower": 3,
        "upper": 4
    },
    "Training Required": {
        "lower": 4,
        "upper": 5
    },
    "Leave The Company": {
        "lower": 5,
        "upper": None
    }
}


for key, value in efficieny.items():
    if value['upper'] == None:
        print(key)
    elif timeTakenByTheWorkerInHours >= value['lower'] and timeTakenByTheWorkerInHours <= value['upper']:
        print(key)
        break
