import pandas as pd

df = pd.read_csv("district_msme_final.csv")

district = input("Enter District Name: ")

result = df[
    df["district_name"].str.lower() == district.lower()
]

if len(result) > 0:
    print(result[[
        "district_name",
        "total",
        "competition"
    ]])
else:
    print("District not found")
