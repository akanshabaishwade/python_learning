# ek global list jiska naam myUniquelist h aur jo khali h
myUniqueList = []
mycreditList = []
# yha addlist nam ka function banaya h ek argument pass kiye h jo jiska nam number h
def addlist(number):
    # yha if condition use kiye h jha ye check h kiya ja rha h argument(number) List(myUniquelist) me hai ya nahi
    if number not in myUniqueList:
        # next line me global list(myUniquelist) me append agrgument(number) kiya ja rha h append ka use pure list ya ek element ko use krne k liye jata h
        myUniqueList.append(number)
        # agr ye condition True hoga to  list me argument ko add n krenge and return  False krenge

        return False
    # yha else condition ka use kiya gya hai age if condition false h to else True ho jaega aur else me jo return krenge wo result me prite hoga
    else:
        tonyleftover(number)
        # yha return kiya ja rha h
        return True

def tonyleftover(number):
    mycreditList.append(number)

# printing and calling addlist with 2
print(addlist(2))
print(addlist(3))
print(addlist(72))
print(addlist(2))
print(addlist("Akasha"))
print(addlist("priya"))
print(addlist("priya"))
addlist(4)

# yha myuniquelist ko print kiya ja rha h
print(myUniqueList)
print(mycreditList)
