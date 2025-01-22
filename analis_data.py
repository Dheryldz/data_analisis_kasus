import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat dataframe dari data yang diberikan
data = {
    "Cakupan": [
        "KABUPATEN SAMBAS", "KABUPATEN BENGKAYANG", "KABUPATEN LANDAK",
        "KABUPATEN MEMPAWAH", "KABUPATEN SANGGAU", "KABUPATEN KETAPANG",
        "KABUPATEN SINTANG", "KABUPATEN KAPUAS HULU", "KABUPATEN SEKADAU",
        "KABUPATEN MELAWI", "KABUPATEN KAYONG UTARA", "KABUPATEN KUBU RAYA",
        "KOTA PONTIANAK", "KOTA SINGKAWANG"
    ],
    "Fisik": [0, 0, 8, 7, 7, 43, 11, 4, 1, 0, 0, 7, 9, 4],
    "Psikis": [0, 0, 0, 1, 5, 45, 3, 0, 0, 0, 1, 9, 11, 5],
    "Seksual": [0, 3, 2, 1, 2, 3, 3, 0, 0, 0, 1, 2, 6, 3],
    "Eksploitasi": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "TPPO": [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Penelantaran": [0, 1, 0, 0, 1, 53, 0, 0, 0, 0, 0, 2, 4, 0],
    "Lainnya": [0, 1, 0, 0, 10, 1, 6, 0, 1, 0, 0, 2, 3, 2]
}

df = pd.DataFrame(data)

# Menghitung total kasus per kategori
total_per_kategori = df.sum(numeric_only=True)

# Menampilkan total kasus per kategori
print("Total kasus per kategori:\n", total_per_kategori)

# Menampilkan total kasus per cakupan (kabupaten/kota)
df["Total Kasus"] = df.iloc[:, 1:].sum(axis=1)
print("\nTotal kasus per daerah:\n", df[["Cakupan", "Total Kasus"]])

# Visualisasi total kasus per daerah
plt.figure(figsize=(12, 6))
sns.barplot(x="Total Kasus", y="Cakupan", data=df, palette="viridis")
plt.title("Distribusi Total Kasus per Daerah")
plt.xlabel("Jumlah Kasus")
plt.ylabel("Daerah")
plt.show()

# Visualisasi distribusi kategori kasus
total_per_kategori.plot(kind="bar", figsize=(10, 5), color="skyblue")
plt.title("Total Kasus Berdasarkan Kategori")
plt.xlabel("Kategori")
plt.ylabel("Jumlah Kasus")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Menampilkan persentase kasus berdasarkan kategori
persentase_kategori = (total_per_kategori / total_per_kategori.sum()) * 100
print("\nPersentase kasus berdasarkan kategori:\n", persentase_kategori)
