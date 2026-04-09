import pandas as pd
import glob

crime_files = glob.glob("data/crime/*.csv")

total_crimes = 0

for file in crime_files:
    try:
        df = pd.read_csv(file)

        if "DISTRICT" in df.columns:
            bengaluru_rows = df[
                df["DISTRICT"].str.contains("BANGALORE|BENGALURU", case=False, na=False)
            ]

            total_crimes += len(bengaluru_rows)

    except:
        continue

print("Estimated Bengaluru crime entries:", total_crimes)