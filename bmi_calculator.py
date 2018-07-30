# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

# Creates function bmi. converts weight and height to calculate bmi index


def bmi():
  weight = float(input("Enter your weight in lbs: ")) * 0.45
  height1 = (float(input("Enter your height in feet: ")) * 12) * 0.0254
  height2 = float(input("Enter your remaining height in inches: ")) * 0.0254
  height = height1 + height2
  bmi = round(weight / (height ** 2))

  # Control flow that determines weight class
  if bmi < 18.5:
    result = "You are under weight."
  elif 18.5 <= bmi <= 24.9:
    result = "You are normal weight."
  elif 25 <= bmi <= 29.9:
    result = "You are over weight."
  else:
    result = "You are obese."

  return("Your BMI is {}.{}".format(bmi, result))


print(bmi())
