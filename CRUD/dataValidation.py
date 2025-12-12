def input_valid(label) -> str:
    while True:
        masukan =  input(label)
        if masukan.strip() != "":
            return masukan
        
        print("Error, Input Tidak Sesuai. Masukan Ulang...")