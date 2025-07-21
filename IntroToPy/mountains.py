import pandas as pd

# Citește fișierul TSV (fără antet, deci header=None)
df = pd.read_csv("IntroToPy/mountains_db.tsv", sep="\t", header=None, names=["Nume", "Altitudine", "Tara", "Cod ISO"])
df = df.replace("NULL", pd.NA)
# Convertește coloana 'Altitudine' în numere
df["Altitudine"] = pd.to_numeric(df["Altitudine"], errors="coerce")

# 1. Număr total de țări
print("1. Număr țări:", df["Tara"].nunique())

# 2. Număr de munți fără altitudine
print("2. Munți fără altitudine:", df["Altitudine"].isna().sum())

#3. Statistici altitudine
alt = df["Altitudine"].dropna()
print("3. Statistici altitudine:")
print("   - Min:", df["Altitudine"].min())
print("   - Max:", df["Altitudine"].max())
print("   - Medie:", df["Altitudine"].mean())
print("   - Mediană:", df["Altitudine"].median())
print("   - Deviație standard:", df["Altitudine"].std())
print(df["Altitudine"].describe())

# 4. Top cei mai înalți munți
topN = 69
top = df.dropna(subset=["Altitudine"]).sort_values(by="Altitudine", ascending=False).head(topN)
print(f"4. Cei mai înalți {topN} munți:")
print(top[["Nume", "Altitudine", "Tara"]].to_string(index=False))