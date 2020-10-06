#sys.argv is a list in Python, which contains the command-line arguments passed to the script.
#(Remember that sys.argv[0] is the name of the script.
import sys
print("This is the name of the file " + sys.argv[0])
print ("Number of arguments " + str(len(sys.argv)))
print ("The arguments are " + str(sys.argv[1:]))