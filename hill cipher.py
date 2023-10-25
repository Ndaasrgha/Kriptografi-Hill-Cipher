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

    # Tambahkan 'X' jika panjang pesan ganjil
    if len(pesan_angka) % 2 != 0:
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
    det_kunci = (kunci[0, 0] * kunci[1, 1] - kunci[0, 1] * kunci[1, 0]) % 26
    det_inv = pow(int(det_kunci), -1, 26)  # Convert det_kunci to regular Python integer

    kunci_invers = np.array([[kunci[1, 1], -kunci[0, 1]], [-kunci[1, 0], kunci[0, 0]]]) * det_inv % 26

    pesan_asli_angka = np.dot(pesan_terdekripsi_matriks, kunci_invers) % 26

    # Ubah angka kembali menjadi huruf
    pesan_asli = ''.join([angka_ke_huruf(angka) for angka in pesan_asli_angka.flatten()])
    return pesan_terdekripsi_matriks, pesan_asli

# Pesan yang akan dienkripsi
plain_text = "AMANDA"

# Enkripsi
pesan_matriks, pesan_terenkripsi, pesan_terenkripsi_teks = enkripsi(plain_text, kunci)
print("Pesan Matriks Terenkripsi:")
print(pesan_matriks)
print("Pesan Terenkripsi:", pesan_terenkripsi_teks)

# Dekripsi
pesan_terdekripsi_matriks, pesan_terdekripsi_teks = dekripsi(pesan_terenkripsi_teks, kunci)
print("Pesan Matriks Terdekripsi:")
print(pesan_terdekripsi_matriks)
print("Pesan Terdekripsi:", pesan_terdekripsi_teks)
