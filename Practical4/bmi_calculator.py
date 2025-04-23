#input weight and height
#calculate BMI according to the equation BMI = weight/(height)**2
#use if-elif-else to adapt to three circumstances: BMI>30, BMI<18.5, and others
#print the result

weight = 67  
height = 1.81  
BMI = weight/(height)**2  


if BMI > 30:  
    print("your BMI is", str(BMI), ", and you are categorized as obese.")#if BMI>30, obese
elif BMI < 18.5:
    print("your BMI is", str(BMI), ", and you are categorized as underweight.")#if BMI<18.5, underweight
else:
    print("your BMI is", str(BMI), ", and you are categorized as normal.")#other circumstances, normal