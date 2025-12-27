from prettytable import PrettyTable
from CRUD import Database, dataValidation
import csv

nama_file = Database.nama_file

def read_data() -> None: 
    # Inisiasi Tabel
    tabel = PrettyTable()

    # Open File Database
    with open(nama_file, "r") as file:
        reader = csv.reader(file)
        try:
            # Membuat Header Tabel
            header = next(reader)
            tabel.field_names = header

            # Memasukkan data ke dalam baris tabel
            for row in reader:
                tabel.add_row(row)

        # Jika Data Kosong
        except StopIteration:
            print("Csv Kosong...")
            return None
        
        # Print Tabel
        tabel.align = "c"
        print(tabel)

def create_data() -> None:
    # Minta Input User
    while True:
        NPM = dataValidation.input_valid("Masukkan NPM: ")
        # Validasi Data NPM
        # Jika NPM sudah ada minta user menginput ulang
        if dataValidation.npm_exist(NPM):
            print("NPM Sudah Terdaftar.")
        else:
            break
    nama = dataValidation.input_valid("Masukkan Nama: ")
    fakultas = dataValidation.input_valid("Masukkan Fakultas: ")
    prodi = dataValidation.input_valid("Masukkan Prodi: ")

    # Membuat Data Baru
    data_baru = [NPM, nama, fakultas, prodi]

    # Memasukkan Data baru ke File
    with open(nama_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data_baru)

def delete_data() -> None:
    # Menampilkan Data Yang sudah ada
    read_data()
    print()

    # Meminta input NPM yang ingin di hapus
    target = dataValidation.input_valid("Masukkan NPM Mahasiswa Yang Ingin DI Hapus: ")

    # data_sementara untuk menyimpan semua data yang tidak di hapus
    # deleted untuk menentukan ada atau tidaknya data yang akan dihapus
    data_sementara = []
    deleted = False

    with open(nama_file, "r") as file:
        reader = csv.reader(file)
        for baris in reader:
            # Mengecek setiap NPM yang ada
            if baris[0] == target:
                print(f"Menghapus Data : {baris[1]} - {baris[0]}")
                # two step verification
                proceed = input("Yakin Ingin Menghapus Data? (Y/n) ")
                if proceed.upper() == "Y":
                    deleted = True
            else:
                # Jika data NPM tidak sesuai dengan yang ingin di hapus,
                # Data akan di append ke data_sementara
                data_sementara.append(baris)
    
    # Menghapus data
    if deleted:
        with open(nama_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data_sementara)
        print("\nData Berhasil Di Hapus.")
    else:
        print("\nData tidak ditemukan.")

def update_data() -> None:
    read_data()
    print()

    target = input("Masukkan NPM Mahasiswa yang ingin di ubah: ")

    data_sementara = []
    updated = False

    with open(nama_file, "r") as file:
        reader = csv.reader(file)
        for baris in reader:
            if baris[0] == target:
                print("Data Ditemukan")
                proceed = input("Yakin ingin mengubah Data? (Y/n)")
                if proceed.upper() == "Y":
                    nama_baru = input("Masukkan Nama (Kosongkan Jika Tidak Ingin Di Ubah): ") or baris[1]
                    jurusan_baru = input("Masukkan Jurusan (Kosongkan Jika Tidak Ingin Di Ubah): ") or baris[3]
                    data_sementara.append([baris[0], nama_baru, baris[2], jurusan_baru])
                    updated = True
            else:
                data_sementara.append(baris)
    
    if updated:
        with open(nama_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data_sementara)
        print("\nData berhasil diubah")
    else:
        print("\nData tidak ditemukan")
      