hitung = 3
while hitung > 0:
    print("Hitung mundur:", hitung)
    hitung -= 1
for i in range(1, 11):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)
