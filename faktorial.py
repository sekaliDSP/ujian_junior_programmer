#3
def faktor():
    number = int(input("masukkan angka yang ingin dihitung!"))
    ulang = 1
    for i in range(1, number+1):
        ulang *= i

    print(ulang)

faktor()