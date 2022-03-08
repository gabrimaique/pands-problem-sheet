# the user is asked to enter a sentence(string)
# each character in a string has a corresponding numerical value(first 0)
sentence = input("Please enter a sentence:")
# the format [::-2] shows the full string every second value backwards
# [slicing start point:slicing end point:steps taken while slicing]
# the start and end point are left blank to include the entire string
# the steps is set to -2 (starts the slicing in reverse and includes every second letter)
print (sentence [::-2])

 