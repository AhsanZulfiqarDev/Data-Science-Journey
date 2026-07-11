def checkIfNotNumeric(*args):
    retValue =True
    for x in args:
        if not (isinstance(x,(int,float))):
            return False
    return True

def addAllNumerics(*args):
    s = 0
    for x in args:
        s += x
    return s
    
if __name__ == "__main__":
    print(addAllNumerics(1, 2, 3, 4, 5))