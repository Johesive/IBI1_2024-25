weight = 67  #input weight
height = 1.81  #input height
BMI = weight/(height)**2  #calculate BMI according to the equation

##use if-elif-else to adapt to three circumstance

if BMI > 30:  
    print("your BMI is", str(BMI), ", and you are categorized as obese.")#if BMI>30, obese
elif BMI < 18.5:
    print("your BMI is", str(BMI), ", and you are categorized as underweight.")#if BMI<18.5, underweight
else:
    print("your BMI is", str(BMI), ", and you are categorized as normal.")#other circumstances, normal