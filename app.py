lst = []
adet = int(input('Kaç Sayı Girilecek: '))
for n in range(adet):
    sayi = int(input('Sayıyı Gir: '))
    lst.append(sayi)
print("Liste İçindeki En Büyük Sayı :", max(lst), "\nListe İçindeki En Büyük Sayı :", min(lst))
