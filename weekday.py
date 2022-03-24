# importing datatime module to access the current date and time
import datetime

# this will automatiically set the corretct date
date = datetime.datetime.now()
# strtime converts into a string
# %A returns the whole day format
today = date.strftime("%A")
# if and else statment 
# if it is saturday it will print from the if 
if today == 'Saturday':
    print("It is the weekend, yay!")
# if its sunday it will print form the elif
elif today == 'Sunday':
    print("It is the weekend, yay!")  
# if it is not saturday or sunday it will prnt the else    
else:
    print("Yes, unfortunately today is a weekday.")



