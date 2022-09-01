height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_float = float(height)
weight_int = int(weight)

bmi = weight_int / (height_float * height_float)

print("Your BMI is " + str(bmi))