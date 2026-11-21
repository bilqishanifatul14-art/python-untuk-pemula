def sapa(nama):
    return f"Halo, {nama}!"

def pangkat(angka, n=2):
    return angka ** n

def jumlah(*angka):
    return sum(angka)

print(sapa("Bilqis"))
print(pangkat(4), pangkat(2, 5))
print(jumlah(1, 2, 3, 4))
