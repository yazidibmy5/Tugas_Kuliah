# 1. Input data
nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

# 2. Perulangan agar transaksi bisa dilakukan berkali-kali
while True:
    print("\n=== MENU TRANSAKSI ===")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")

    # 3. Pilih transaksi
    pilihan = input("Pilih transaksi (1/2/3): ")

    # 4. Proses transaksi dengan percabangan
    if pilihan == "1":
        jumlah = int(input("Jumlah barang masuk: "))
        stok = stok + jumlah
        print(f"Barang masuk berhasil. Stok {nama_barang} sekarang: {stok}")

    elif pilihan == "2":
        jumlah = int(input("Jumlah barang keluar: "))

        # 5. Percabangan untuk cek ketersediaan stok
        if jumlah > stok:
            print("Stok Tidak Mencukupi")
        else:
            stok = stok - jumlah
            print(f"Barang keluar berhasil. Stok {nama_barang} sekarang: {stok}")

    elif pilihan == "3":
        print("\nTransaksi selesai.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")

# 6. Tampilkan hasil akhir
print("\n=== HASIL AKHIR ===")
print(f"Nama Barang : {nama_barang}")
print(f"Stok Akhir  : {stok}")