from prettytable import PrettyTable
from CRUD import Database, dataValidation
import csv

nama_file = Database.nama_file

def read_data() -> None: 
    tabel = PrettyTable()

    with open(nama_file, "r") as file:
        reader = csv.reader(file)
        try:
            header = next(reader)
            tabel.field_names = header

            for row in reader:
                tabel.add_row(row)

        except StopIteration:
            print("Csv Kosong...")
            return None
        
        # Print Tabel
        tabel.align = "c"
        print(tabel)

def create_data() -> None:
    print("Membuat....")
    while True:
        NPM = dataValidation.input_valid("Masukkan NPM: ")
        if dataValidation.npm_exist(NPM):
            print("NPM Sudah Terdaftar.")
        else:
            break
    nama = dataValidation.input_valid("Masukkan Nama: ")
    fakultas = dataValidation.input_valid("Masukkan Fakultas: ")
    prodi = dataValidation.input_valid("Masukkan Prodi: ")

    data_baru = [NPM, nama, fakultas, prodi]

    with open(nama_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data_baru)

if __name__ == "__main__":
    create_data()
