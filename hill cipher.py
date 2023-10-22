import numpy as np

# Matriks kunci enkripsi 2x2
kunci = np.array([[3, 2], [5, 7]])

# Fungsi untuk mengonversi huruf menjadi angka
def huruf_ke_angka(huruf):
    return ord(huruf) - ord('A')

# Fungsi untuk mengonversi angka kembali menjadi huruf
def angka_ke_huruf(angka):
    return chr(angka + ord('A'))

# Fungsi untuk mengenkripsi pesan
def enkripsi(pesan, kunci):
    pesan = pesan.upper()
    pesan_angka = [huruf_ke_angka(huruf) for huruf in pesan]

    if len(pesan) % 2 != 0:
        pesan_angka.append(huruf_ke_angka('X'))

    pesan_matriks = np.array(pesan_angka).reshape(-1, 2)
    pesan_terenkripsi = np.dot(pesan_matriks, kunci) % 26

    hasil_terenkripsi = ''.join([angka_ke_huruf(angka) for angka in pesan_terenkripsi.flatten()])
    return pesan_matriks, pesan_terenkripsi, hasil_terenkripsi

# Fungsi untuk mendekripsi pesan
def dekripsi(pesan_terenkripsi, kunci):
    pesan_terenkripsi = pesan_terenkripsi.upper()
    pesan_terenkripsi_angka = [huruf_ke_angka(huruf) for huruf in pesan_terenkripsi]
    pesan_terdekripsi_matriks = np.array(pesan_terenkripsi_angka).reshape(-1, 2)

    # Matriks invers dari kunci
    kunci_invers = np.linalg.inv(kunci)
    kunci_invers = np.round(kunci_invers).astype(int)  # Bulatkan ke bilangan bulat

    pesan_asli_angka = np.dot(pesan_terdekripsi_matriks, kunci_invers) % 26

    # Ubah angka kembali menjadi huruf
    pesan_asli = ''.join([angka_ke_huruf(angka) for angka in pesan_asli_angka.flatten()])
    return pesan_terdekripsi_matriks, pesan_asli

#enkripsi
pesan = "SARAGIH"
pesan_matriks, pesan_terenkripsi, pesan_terenkripsi_teks = enkripsi(pesan, kunci)
print("Pesan Matriks Terenkripsi:")
print(pesan_matriks)
print("Pesan Terenkripsi:", pesan_terenkripsi_teks)

#dekripsi
pesan_terenkripsi = "IGNNJG"
pesan_terdekripsi_matriks, pesan_terdekripsi_teks = dekripsi(pesan_terenkripsi, kunci)
print("Pesan Matriks Terdekripsi:")
print(pesan_terdekripsi_matriks)
print("Pesan Terdekripsi:", pesan_terdekripsi_teks)
