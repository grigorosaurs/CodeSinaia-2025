import csv
import statistics

# Funcția care încarcă datele din fișier
def load_data(mountaints_db):
    mountains = []

    # Deschidem fișierul
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter="\t")  # Fișierul este TSV, deci separăm prin TAB

        # Citim fiecare linie
        for row in reader:
            name = row[0]
            altitude = row[1] 
            country = row[2]
            iso = row[3]

            # Dacă altitudinea este cunoscută, o transformăm în număr
            if altitude != "NULL":
                altitude = int(altitude)
            else:
                altitude = None

            # Adăugăm muntele în listă
            mountains.append({
                "name": name,
                "altitude": altitude,
                "country": country,
                "iso": iso
            })

    return mountains


# Funcția care calculează cerințele 1–3
def analyze(mountains):
    # Cerința 1: Număr total de țări diferite
    all_countries = {m["country"] for m in mountains}
    print("1. Număr total de țări diferite:", len(all_countries))

    # Cerința 2: Munți fără altitudine
    missing = [m for m in mountains if m["altitude"] is None]
    print("2. Număr munți fără altitudine:", len(missing))

    # Cerința 3: Statistici altitudine (doar pentru cei cu valoare)
    altitudes = [m["altitude"] for m in mountains if m["altitude"] is not None]

    if altitudes:
        print("3. Statistici altitudine:")
        print("   - Minim:", min(altitudes), "m")
        print("   - Maxim:", max(altitudes), "m")
        print("   - Medie:", round(sum(altitudes) / len(altitudes), 2), "m")
        print("   - Mediană:", statistics.median(altitudes), "m")
        print("   - Abatere standard:", round(statistics.stdev(altitudes), 2), "m")
    else:
        print("Nu există munți cu altitudine cunoscută.")


# Cerința 4: Top N munți cei mai înalți
def top_mountains(mountains, N=5):
    # Selectăm doar munții cu altitudine
    known = [m for m in mountains if m["altitude"] is not None]
    
    # Sortăm descrescător după altitudine
    top = sorted(known, key=lambda m: m["altitude"], reverse=True)[:N]

    print(f"\n4. Cei mai înalți {N} munți:")
    for m in top:
        print(f"{m['name']} ({m['altitude']} m) - {m['country']} [{m['iso']}]")



# Funcția principală
if __name__ == "__main__":
    file = "mountains_db.tsv"  # Asigură-te că fișierul este în același folder
    mountains = load_data
