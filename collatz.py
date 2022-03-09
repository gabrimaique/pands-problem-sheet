# the user input a positive integer
number = int(input("please enter a positive whole number:"))
# list is used to store multiple items in a single variable
mylist = []
# users input is appended to the list
mylist.append(number)
# if statement to check if the user has input a positive number
if number <= 0:
    print("no negativity or zeros allowed here")
# while loop checks if the number is not equal to 1
while number != 1:
    # the if statement verify if the number is odd or even
    if (number % 2) == 0:
        number = (number//2) # divides the number by 2
        mylist.append(number)

    else:
        number = int(3*number +1) # if the number is odd it's multiplied by three and one is added
        # adds the output of the while loop to the list numbers
        mylist.append(number) 

print(mylist)        