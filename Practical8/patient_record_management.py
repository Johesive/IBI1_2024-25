#create class
#define init: self, patient_name, age, date_of_latest_admission, medical_history
#self.patient_name = patient_name
#self.age = age
#self.date_of_latest_admission = date_of_latest_admission
#self.medical_history = medical_history
#def print_details(self):
#print "Name:self.patient_name, Age:self.age, Latest Admission Date: self.date_of_latest_admission, Medical History: self.medical_history"


class patients:
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history):
        self.patient_name = patient_name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def print_details(self):
        print(f"Name: {self.patient_name}, Age: {self.age}, Latest Admission Date: {self.date_of_latest_admission}, Medical History: {self.medical_history}")


patient = patients("Zhejiong Chen", 18, "2024-07-03", "Penicillin allergy")  #input
patient.print_details()