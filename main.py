fileName = input("what file name do you want to create? ")
# type in a example file, either a new one or one shown on the left pane
import os
# if statement will work on existing files from the left pane
if os.path.exists(fileName):
  os.remove(fileName)
  print("file exists!")

# x is to create
f = open(fileName, "x")
f.close()

# w is to write
f = open(fileName, "w")
f.write("welcome to my file\n")

# a is to append
f = open(fileName, "a")
for i in range(5):
  f.write("This is line %d\r\n" % (i+1))

# is to read
f = open(fileName, "r")
print(f.read())

f.close()