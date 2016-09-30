import random

no_of_patients=5
no_of_doctors=5

patient_list_with_preference = [[0 for x in range(no_of_patients)] for y in range(no_of_doctors)] 
doctor_list_with_preference = [[0 for x in range(no_of_patients)] for y in range(no_of_doctors)]

taken_once=[]

for i in range(no_of_patients):
	for j in range(no_of_doctors):
		random_doctor=random.randrange(0,no_of_doctors)
		if random_doctor not in taken_once:
			taken_once.append(random_doctor)
			patient_list_with_preference[i][j]=random_doctor
		else:
			while random_doctor in taken_once:
				random_doctor=random.randrange(0,no_of_doctors)
		taken_once.append(random_doctor)
		patient_list_with_preference[i][j]=random_doctor
	del taken_once[:]

print patient_list_with_preference			

del taken_once[:]

for i in range(no_of_doctors):
	for j in range(no_of_patients):
		random_patient=random.randrange(0,no_of_patients)
		if random_patient not in taken_once:
			taken_once.append(random_patient)
			doctor_list_with_preference[i][j]=random_patient
		else:
			while random_patient in taken_once:
				random_patient=random.randrange(0,no_of_patients)
			taken_once.append(random_patient)
			doctor_list_with_preference[i][j]=random_patient	
	del taken_once[:]

del taken_once[:]

print doctor_list_with_preference	

doctors_alloted_to_patients=[]

for i in range(no_of_patients):
	random_doctor=random.randrange(0,no_of_doctors)
	while random_doctor in taken_once:
		random_doctor=random.randrang(e0,no_of_doctors)	
	doctors_alloted_to_patients.append(random_doctor)
	taken_once.append(random_doctor)

print doctors_alloted_to_patients

