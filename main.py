import csv
import prettytable as pt
import os

if __name__ == "__main__":
    sistem_operasi = os.name

    while True:
        match sistem_operasi:
            case "nt": os.system("cls")
            case "posix": os.system("clear")
        print("CRUD APLICATION")
        print("made by: Ziyad Aditya.")
        print("----------------------")

        # Choice
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        pilihan = input("Pilihan Mu... ")
        print()

        match pilihan:
            case "1":
                print("Read Data...")
            case "2":
                print("Create Data...")
            case "3":
                print("Update Data...")
            case "4":
                print("Delete Data...")
            case _ :
                print("Invalid Choice...")
        
        is_selesai = input("Selesai (Y/n)? ... ") 
        if is_selesai.upper() == "Y":
            break