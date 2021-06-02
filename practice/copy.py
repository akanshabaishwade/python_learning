myUniqueList = []
myLeftovers = []

def addTomyUniqueList (anything):
    if not anything in myUniqueList:
        myUniqueList.append(anything)
        return True
    else:
        addTomyLeftovers(anything)
        return False

def addTomyLeftovers(anything):
    myLeftovers.append(anything)


print(myUniqueList)
print(addTomyUniqueList(1))
print(addTomyUniqueList(2))
print(addTomyUniqueList(3))
print(myUniqueList)

print(myLeftovers)
print(addTomyUniqueList(1))
print(addTomyUniqueList(2))
print(myUniqueList)
print(myLeftovers)