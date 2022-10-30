def calculate_bmi(height, weight):
        print("Height = " + str(height))
        print("Weight = " + str(weight))

        bmi = weight/(height*height)

        print("BMI = " + str(bmi))

        if(bmi < 18.5):
            return("Under weight")

        elif (bmi >= 18.5 and bmi <= 25.0):
            return("Normal weight")

        else:
            return("Overweight")

print (calculate_bmi(height=1.73, weight=57))
