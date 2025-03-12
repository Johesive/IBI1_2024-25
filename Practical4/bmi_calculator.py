weight = 67  #input weight
height = 1.81  #input height
BMI = weight/(height)**2  #calculate BMI

if BMI > 30:  #use if-elif-else to adapt to three circumstances
    print("your BMI is", str(BMI), ", and you are categorized as obese.")
elif BMI < 18.5:
    print("your BMI is", str(BMI), ", and you are categorized as underweight.")
else:
    print("your BMI is", str(BMI), ", and you are categorized as normal.")