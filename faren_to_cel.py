def celToFarenhit():
    noCel=float(input("Please enter celcius:"))
    return (noCel*(9/5) + 32)
print(celToFarenhit())

def farenhitToCel():
    noFar=float(input("Please enter celcius:"))
    return (noFar*(5/9) - 32)
print(farenhitToCel())