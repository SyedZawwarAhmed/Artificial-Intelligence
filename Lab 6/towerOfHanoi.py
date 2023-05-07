steps = 0
def towerOfHanoi(numberOfDisks, fromRod, toRod, auxRod):
    global steps
    if numberOfDisks == 1:
        print("Disk 1 from rod", fromRod, 'to rod', toRod)
        steps += 1
        return

    towerOfHanoi(numberOfDisks-1, fromRod, auxRod, toRod)
    print("Disk", numberOfDisks, "from rod", fromRod, 'to rod', toRod)
    steps += 1
    towerOfHanoi(numberOfDisks-1, auxRod, toRod, fromRod)


if __name__ == '__main__':
    towerOfHanoi(5, "A", "C", "B")
    print("It took", steps, 'steps')
