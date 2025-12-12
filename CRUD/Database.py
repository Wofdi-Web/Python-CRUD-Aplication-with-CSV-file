import os
import csv

nama_file = "mahasiswa.csv"

def init_data():
    if not os.path.exists(nama_file):
        with open(nama_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["NPM", "NAMA", "FAKULTAS", "PRODI"])
