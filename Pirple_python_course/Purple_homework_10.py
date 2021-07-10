
import array

arr = array.array('i', [1, 2, 3, 1, 5])

print ("created array : ", end ="")
for i in range (0, 5):
	print (arr[i], end =" ")

print ("\r")

print ("after Remove duplicate item : ", end ="")
print (arr.pop(2))

print ("before remove duplicage item : ", end ="")
for i in range (0, 4):
	print (arr[i], end =" ")

print("\r")

arr.remove(1)

print ("removing item list : ", end ="")
for i in range (0, 3):
	print (arr[i], end =" ")
