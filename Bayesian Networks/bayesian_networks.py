from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough')
])

cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.9], [0.1]]
)

cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[
        [0.8, 0.2],
        [0.2, 0.8]  
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_cough = TabularCPD(
    variable='Cough',
    variable_card=2,
    values=[
        [0.7, 0.3], 
        [0.3, 0.7] 
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

model.add_cpds(cpd_disease, cpd_fever, cpd_cough)

print("Model Valid:", model.check_model())

infer = VariableElimination(model)

print("\nEnter Symptom Information")
print("0 = No, 1 = Yes")

fever = int(input("Do you have fever? (0/1): "))
cough = int(input("Do you have cough? (0/1): "))

result = infer.query(
    variables=['Disease'],
    evidence={
        'Fever': fever,
        'Cough': cough
    }
)

print("\nProbability of Disease:")
print(result)
