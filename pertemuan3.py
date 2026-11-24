class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim


mhs = Mahasiswa("Ibra", "14022500032")
print(mhs.nama)
print(mhs.nim)