from prettytable import PrettyTable
import csv
from CRUD import Database

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

if __name__ == "__main__":
    read_data()
