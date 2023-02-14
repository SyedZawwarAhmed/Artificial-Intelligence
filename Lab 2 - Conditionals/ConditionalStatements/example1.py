a = int (input ("Enter a number and I'll get its square root: "))
if (a > 0):
    print ("The number you entered is greater than 0, so I can calculate it!")
    root = a** (1/2)
    print ("The square root of %d is %f" % (a, root))
if (a <= 0) :
    print ("I can't calculate the square root of a negative number!")
print ("Thanks for the input!")