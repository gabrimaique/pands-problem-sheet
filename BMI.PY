#first we need to ask their height and weight
#we must convert string to float
height = float(input("Input your height in Cm: ")) #coding for weight
weight = float(input("Input your weight in Kilogram: ")) #coding for height
#the formula to calculate the BMI is BMI = kg/m2
BMI = weight / (height/100)**2
#let's print out the BMI
print(f"You BMI is {BMI}")