def drug_dosage_calculator(weight, strength):
    if strength == 120 or strength == 250: 
        if 10 <= weight <= 100:
            recommended_dosage = weight * 15  #calculate the recommended dosage
            recommended_volume = recommended_dosage/(strength/5)  #calculate the recommended volume
            return int(recommended_volume)  #return the recommended volume in integer
        else:
            print("The supplied weight is outwith the expected range.")  #situation when the weight is not in the range of 10-100
    else:
        print("The paracetamol strength does not match an expected concentration")  #situation when the strength is not 120 or 250


weight = float(input("Enter the weight in kg: "))
strength = float(input("Enter the strength of paracetamol (either 120mg/5ml or 250mg/5ml): "))
print("The recommended volume of paracetamol is:", drug_dosage_calculator(weight, strength),"ml")