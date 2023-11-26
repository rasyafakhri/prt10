def tambah_data():
    nim = input("Masukkan NIM mahasiswa: ")
    nama = input("Masukkan Nama mahasiswa: ")
    nilai_tugas = float(input("Masukkan nilai Tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    nilai_akhir = (0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)
    data_mahasiswa[nim] = {
        'Nama': nama,
        'Nilai Tugas': nilai_tugas,
        'Nilai UTS': nilai_uts,
        'Nilai UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir
    }
    print("Data mahasiswa telah ditambahkan!")

def tampilkan_data():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa yang tersimpan.")
    else:
        print("===== DAFTAR NILAI MAHASISWA =====")
        print("{:<10} {:<20} {:<15} {:<15} {:<15} {:<15}".format(
            "NIM", "Nama", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Nilai Akhir"))
        for nim, data in data_mahasiswa.items():
            print("{:<10} {:<20} {:<15} {:<15} {:<15} {:<15}".format(
                nim, data['Nama'], str(data['Nilai Tugas']), str(data['Nilai UTS']), str(data['Nilai UAS']), str(data['Nilai Akhir'])))

def cari_data():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa yang tersimpan.")
    else:
        nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
        if nim in data_mahasiswa:
            print("===== DATA MAHASISWA =====")
            print("NIM         :", nim)
            for key, value in data_mahasiswa[nim].items():
                print(key + ':', value)
        else:
            print("NIM tidak ditemukan.")

def ubah_data():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa yang tersimpan.")
    else:
        nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ")
        if nim in data_mahasiswa:
            print("Masukkan data baru:")
            data_mahasiswa[nim]['Nama'] = input("Nama baru: ")
            data_mahasiswa[nim]['Nilai Tugas'] = float(input("Nilai Tugas baru: "))
            data_mahasiswa[nim]['Nilai UTS'] = float(input("Nilai UTS baru: "))
            data_mahasiswa[nim]['Nilai UAS'] = float(input("Nilai UAS baru: "))
            data_mahasiswa[nim]['Nilai Akhir'] = (0.3 * data_mahasiswa[nim]['Nilai Tugas']) + (0.35 * data_mahasiswa[nim]['Nilai UTS']) + (0.35 * data_mahasiswa[nim]['Nilai UAS'])
            print("Data mahasiswa telah diubah!")
        else:
            print("NIM tidak ditemukan.")

def hapus_data():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa yang tersimpan.")
    else:
        nim = input("Masukkan NIM mahasiswa yang ingin dihapus datanya: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data mahasiswa telah dihapus!")
        else:
            print("NIM tidak ditemukan.")

data_mahasiswa = {}

while True:
    print("\n===== MENU PILIHAN =====")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka 1-6.")
