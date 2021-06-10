import pandas as pd

data = pd.read_csv('output_readings/final_processed_data.csv')
metrics = pd.read_csv('output/avg_patient_metrics.csv')

for i in metrics:
    print(i)
    