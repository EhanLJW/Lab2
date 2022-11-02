print("ET0735 (DevOps for AIoT) - Lab 2 - Intoduction to Python")

def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

#Add code here to calculate BMI
    bmi_height = float(height)
    bmi_weight = float(weight)
    bmi_total = bmi_weight/((bmi_height)*(bmi_height))

    if (bmi_total < 18.5):
        print("under weight")

    elif(18.5 <= bmi_total <= 25):
        print("normal weight")

    else:
        print("over weight")

    print("BMI = "+ str(bmi_total) )

#Add code here to display calculate BMI
calculate_bmi(57, 1.73)