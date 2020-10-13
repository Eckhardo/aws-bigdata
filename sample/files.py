import csv
import time
import sys
sourceData = "orders.txt"
destinationData = "writeToFile.txt"
destinationData
myinput = open(sourceData)
print('Current Position: {}' .format(myinput.tell()))

for i, l in enumerate(myinput):
 
    pass
print("Reading " + str(i) + " lines ") 

myinput.close()

#  automatically close a file when with ... as is finished:
with open(sourceData, 'r') as inputStream:
    print('File closed ? {}' .format(inputStream.closed))
    file_contents = inputStream.read()
    print('Current Position: {}' .format(inputStream.tell()))
print('File closed ? {}' .format(inputStream.closed))

# Print one line at a time
   
with open(sourceData, 'r') as inputStream:
    for line in inputStream:
        print(line)

print("Write to Destination File") 
with open(destinationData, 'w') as inputStream:
    inputStream.write('This Text will be written to the file. \n')

print("Read from Destination File")     
with open(destinationData, 'r') as inputStream:
    for line in inputStream:
        print(line)

print("Try except when opening a file")
try:
    myinput = open(sourceData).read()
except:
    myinput= ''
print(' Length of file: {}'.format(len(myinput)))
    

