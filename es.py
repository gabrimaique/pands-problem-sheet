#module that let the user read the file as an argument
import sys
#used to read from a text file specified in the command line 
filename = sys.argv[1]
# def function for finding the letters in the txt file
# two variable(arguments) filename and letter
def numberOfe(filename, letter):
# the file is opened as f
    with open(filename) as f:
 #  store content of file in a variable     
        text = f.read() 
        # using count()
        return text.count(letter)
# calling the function
print(numberOfe(filename, 'e'))

  