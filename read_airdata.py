import pandas as pd

# CSV File Name
CSV_FILE = "air_data.csv"

df = pd.read_csv(CSV_FILE)

print(df)
print(df['JSON'])