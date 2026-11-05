import pandas as pd

# Patient dataset
dataset = {
    'PID': [12021, 12022, 12023, 12024, 12025],
    'Wt_kg': [55, 65, 70, 85, 95],
    'Ht_m': [1.55, 1.65, 1.75, 1.85, 1.95]
}

# Create DataFrame
df = pd.DataFrame(dataset)

# Calculate BMI
df['BMI'] = df['Wt_kg'] / (df['Ht_m'] ** 2)

# Classifying BMI of Patients
def classify_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    elif bmi < 35:
        return 'Obesity Class I'
    elif bmi < 40:
        return 'Obesity Class II'
    else:
        return 'Obesity Class III'

df['BMI_Category'] = df['BMI'].apply(classify_bmi)

# Display results
print(df.round(2))
