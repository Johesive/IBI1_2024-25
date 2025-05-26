#define the function drug_dosage_calculator
#if the strength is 120 or 250 and the weight is between 10 and 100:
#calculate the recommended dosage: recommended_dosage = weight * 15  
#calculate the recommended volume: recommended_volume = recommended_dosage/(strength/5) 
#return the recommended volume in integer
#else:
#print "The paracetamol strength does not match an expected concentration" or "The supplied weight is outwith the expected range"


def drug_dosage_calculator(weight, strength):
    if strength == 120 or strength == 250: 
        if 10 <= weight <= 100:
            recommended_dosage = weight * 15  
            recommended_volume = recommended_dosage/(strength/5)  
            return int(recommended_volume) 
        else:
            raise ValueError("The supplied weight is outwith the expected range.")
    else:
        raise ValueError("The paracetamol strength does not match an expected concentration.")  #situation when the strength is not 120 or 250


weight = float(input("Enter the weight in kg: "))
strength = float(input("Enter the strength of paracetamol (either 120mg/5ml or 250mg/5ml): "))
print("The recommended volume of paracetamol is:", drug_dosage_calculator(weight, strength),"ml")