def dash():
    number = str(input("masukkan angka yang ingin dihitung!"))
    keluaran = []
    angka = []
    for i in (str(number)):
        angka.append(int(i))

    for i in range(0,len(angka)):
        if angka[i]%2 == 0:
            try:
                if (angka[i+1])%2 == 0:
                    keluaran.append(angka[i])
                    keluaran.append("-")
                else:
                    keluaran.append(angka[i])
            except Exception  as e:
                keluaran.append(angka[len(angka)-1])
        else:
            keluaran.append(angka[i])
    for i in keluaran:
        print(i, end="")
dash()

