
import numpy as np
import pandas as pd
from scipy.stats import poisson
import random
from random import randint
import datetime
import sys

# RANDOM GENDER GENERATION
def patient_gender():
    sex = ['Male', 'Female']
    for _ in range(1, 500):
        gender = random.choice(sex)
    return gender

# RANDOM AGE GENERATION   
def patient_age():
    ages = ['0-4', '5-19', '20-64', '65+']
    for _ in range(1, 500):
         age = random.choice(ages)
    return age

# RANDOM CONDITION GENERATION 
def patient_condition():
    conditions = ['Unknown', 'Dislocation/fracture/joint injury/amputation', 'Respiratory conditions', 'Central Nervous System conditions', 'Cardiac conditions', 'Collapse', 'Falls', 'Gastrointestinal conditions']
    for _ in range(1, 500):
        condition = random.choice(conditions)
    return condition

# RANDOM AMBULANCE GENERATION
def patient_ambulance():
    for _ in range(1, 500):
        ambulance = random.randint(0,21)
    return ambulance

# RANDOM ASSESSED GENERATION
def patients_assessed():
    for _ in range(0, 500):
        assessed = random.randint(1,334)
    return assessed

# RANDOM OUTCOME GENERATION 
def patient_outcome():
    outcomes = ['Admitted', 'Call closed', 'Discharged', 'Emergency Dentist', 'MIU', 'Not picked up by an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor', 'Spoke to a primary care service', 'WIC']
    for _ in range(1, 500):
        outcome = random.choice(outcomes)
    return outcome 
 
# LOGGING THE PATIENTS' INFORMATION   
def patient_log():
    condition = patient_condition()
    gender = patient_gender()
    age = patient_age()
    ambulance = patient_ambulance()
    assessed = patients_assessed()
    outcome = patient_outcome()

    return [gender, age, condition, outcome, ambulance, assessed]

try:
    NUM_PATIENTS = int(sys.argv[2])
except:
    NUM_PATIENTS = 500


records = lambda x: [patient_log() for _ in range(x)]
a = np.array(records(NUM_PATIENTS))

test = pd.DataFrame()
test['Gender'] = a[:,0]
test['Age'] = a[:,1]
test['Condition'] = a[:,2]
test['outcome'] = a[:,3]
test['Ambulance'] = a[:,4]
test['Assessed'] = a[:,5]
test.index.name='Patient'
outfile = 'patient-data.csv'
test.to_csv(outfile, index=True)
print('generated patients dataset and wrote output into: \n\t{}'.format(outfile))
    
    
