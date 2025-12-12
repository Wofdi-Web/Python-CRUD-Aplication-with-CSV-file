from CRUD import Database
import csv

nama_file = Database.nama_file

def input_valid(label) -> str:
    while True:
        masukan =  input(label)
        if masukan.strip() != "":
            return masukan
        
        print("Error, Input Tidak Sesuai. Masukan Ulang...\n")

def npm_exist(NPM) -> bool:
    with open(nama_file, "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for baris in reader:
            if baris[0] == NPM:
                return True

    return False