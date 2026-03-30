import pandas as pd
########################################################################################################################################################
# Add a column to your file

# # Load your CSV file
# df = pd.read_csv("simus_p3.csv")

# # Add the new column with constant value 0.2
# # df.pop("w [mm]")  # remove existing column
# df.insert(1, "w [mm]", 0.2)  # insert new column at the beginning

# # Save the modified file
# df.to_csv("simus_p3.csv", index=False)

########################################################################################################################################################
# Join files and sort them

# List your CSV files
files = ["simus_p1.csv", "simus_p1_2.csv", "simus_p2.csv", "simus_p2_2.csv", "simus_p3.csv"]
new_header = '"h [mm]","w [mm]","Freq [GHz]","dB(S(Port_In,Port_In)) []","dB(S(Port_Out,Port_In)) []","mag(Zo(Port_In)) []"\n'
dfs = []
# Read and concatenate all files
for file in files:
    print(f"Processing {file}...")
    with open(file, "r") as f:
        lines = f.readlines()
    lines[0] = new_header  # replace first row
    with open(file, "w") as f:
        f.writelines(lines)
    
    df = pd.read_csv(file)  # Automatically detect the separator
    print(df.columns)
    print(df.head())
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

# Sort by "w [mm]" first, then "h [mm]"
df = df.sort_values(by=["w [mm]", "h [mm]"])

# Save the result
df.to_csv("simus.csv", index=False)