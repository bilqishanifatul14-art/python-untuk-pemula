class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Saya {self.nama} dari kelas {self.kelas}"

s1 = Siswa("Bilqis", "X RPL")
s2 = Siswa("Budi", "X RPL")
print(s1.perkenalan())
print(s2.perkenalan())
