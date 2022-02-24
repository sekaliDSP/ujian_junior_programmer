def gaji():
    agus = {"nama":"agus","gaji":8000000, "jabatan":"junior officer", "region": "semarang", "penghasilan":0}
    dina = {"nama":"dina","gaji":15000000, "jabatan":"ass. manager", "region": "bandung", "penghasilan":0}
    joko = {"nama":"joko","gaji":25000000, "jabatan":"manager", "region": "jakarta", "penghasilan":0}
    ahmad = {"nama":"ahmad","gaji":13000000, "jabatan":"middle officer", "region": "jakarta", "penghasilan":0}
    felicia = {"nama":"felicia","gaji":12500000, "jabatan":"middle officer", "region": "bandung", "penghasilan":0}

    nama = [agus, dina, joko, ahmad, felicia]
    hasil = []

    for i in range(len(nama)):
       if nama[i]["gaji"] > 15000000:
            
          nama[i]["penghasilan"] += nama[i]["gaji"] + nama[i]["gaji"] * 0.1

       elif nama[i]["gaji"] < 15000000 and nama[i]["gaji"] >= 10000000:
            
            nama[i]["penghasilan"] += nama[i]["gaji"] + nama[i]["gaji"] * 0.12

       else:
            
            nama[i]["penghasilan"] += nama[i]["gaji"] + nama[i]["gaji"] * 0.15

    for i in range(len(nama)):
       if nama[i]["region"] == "jakarta":

          nama[i]["penghasilan"] += nama[i]["gaji"] - nama[i]["gaji"] * 0.025

       elif nama[i]["region"] == "bandung":

            nama[i]["penghasilan"] += nama[i]["gaji"] - nama[i]["gaji"] * 0.02

       else:

            nama[i]["penghasilan"] += nama[i]["gaji"] - nama[i]["gaji"] * 0.018

    for i in range(len(nama)):
       if nama[i]["jabatan"] == "manager":
            
          nama[i]["penghasilan"] += 250000

       elif nama[i]["jabatan"] == "ass. manager":
            
            nama[i]["penghasilan"] += 175000

       elif nama[i]["jabatan"] == "senior officer":

           nama[i]["penghasilan"] += 150000

       elif nama[i]["jabatan"] == "middle officer":
            
            nama[i]["penghasilan"] += 125000

       else:
            nama[i]["penghasilan"] += 100000

    for i in range(len(nama)):
            kata_kata = "{0} berpenghasilan Rp.{1} / bulan".format(nama[i]["nama"],int(nama[i]["penghasilan"]))

            hasil.append(kata_kata)

    #for i in (hasil):
     #   print(i)
     #karena ingin dalam bentuk list maka printnya yang bawah. jika ingin hasilnya tidak dalam list uncomment yang 2 line di atas dan comment yang di bawah
    print(hasil)

gaji()