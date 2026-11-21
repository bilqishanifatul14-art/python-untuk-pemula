siswa = {"nama": "Bilqis", "kelas": "X", "umur": 16}
siswa["jurusan"] = "RPL"
print(siswa["nama"], siswa.get("kelas"))
for kunci, nilai in siswa.items():
    print(kunci, "=", nilai)
