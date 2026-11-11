# Data target nilai tiap mahasiswa
target_mahasiswa = {
    "andi": 70,
    "budi": 75,
    "citra": 80,
}

MAKS_PERCOBAAN = 3

print("=" * 40)
print("   PROGRAM UJIAN MATEMATIKA & REMEDIAL")
print("=" * 40)

# 1. Input nama mahasiswa dan tampilkan targetnya
nama = input("Nama : ").strip()

while nama.lower() not in target_mahasiswa:
    print("Nama tidak ditemukan! Pilih: Andi, Budi, atau Citra.")
    nama = input("Nama : ").strip()

target = target_mahasiswa[nama.lower()]
nama = nama.capitalize()
print(f"Target nilai {nama}: {target}")
print("-" * 40)

# 2 & 3. Input nilai dan cek target, ulangi maksimal 3 kali
percobaan = 0
lulus = False

while percobaan < MAKS_PERCOBAAN and not lulus:
    percobaan += 1
    nilai = float(input(f"Nilai {percobaan} : "))

    if nilai >= target:
        lulus = True
    else:
        print(f"  -> Nilai {nilai:g} belum mencapai target {target}.")

# 4. Tampilkan hasil akhir
print("-" * 40)
if lulus:
    print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama} tidak lulus setelah {percobaan} kali percobaan!")