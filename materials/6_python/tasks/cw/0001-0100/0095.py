## Calculate BMI

# Write function bmi that calculates body mass index (bmi = weight / height2).

def bmi(weight, height):
    message = ""
    bmi_value = weight / (height * height)
    if bmi_value <= 18.5:
        message = "Underweight"
    elif bmi_value <= 25.0:
        message = "Normal"
    elif bmi_value <= 30:
        message = "Overweight"
    else:
        message = "Obese"
    return message
