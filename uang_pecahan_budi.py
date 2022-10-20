def kembalian():
    uang_budi = 1895250

    seratus = int(uang_budi/100000)
    sisa = uang_budi%100000

    limapuluh = int(sisa/50000)
    sisa = sisa%50000
    
    duapuluh = int(sisa/20000)
    sisa = sisa%20000
    
    limarb = int(sisa/5000)
    sisa = sisa%5000

    seribu = int(sisa/1000)
    sisa = sisa%1000
    
    lp = int(sisa/50)
    sisa = sisa%50

    print("uang kembalian yang diperoleh budi adalah 100.000 sebanyak "
          +str(seratus)+" 50000 sebanyak "+str(limapuluh)+" 20000 sebanyak "
          +str(duapuluh)+" 5000 sebanyak "+str(limarb)+" 1000 sebanyak "+str(seribu)+" 50 sebanyak "+str(lp))

kembalian()