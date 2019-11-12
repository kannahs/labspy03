modal = 100000000                                          ## Nilai modal
laba = 0                                                   ## Nilai laba 0
untung = 0                                                 ## Nilai untung
for i in range(1,9,1):                                     ## perulangan i dengan nilai awal 1, akhir 9 dan step 1
     if(i<3):                                              ## Kondisi apabila belum bulan ke-3 laba masih 0%
         laba = 0
         untung = untung + laba
     elif(i<5):                                            ## Kondisi apabila belum memasuki bulan ke-5, mendapat laba sebesar 1%
         laba = modal*1/100
         untung = untung + laba
     elif(i<8):                                            ## Kondisi apabila belum memasuki bulan ke-8, mendapat laba sebesar 5%
         laba = modal*5/100
         untung = untung + laba
     else:                                                 ## Pada bulan ke-8 laba menurun 2%, sehingga laba bulan ke-8 sebesar 3%
         laba = modal*2/100
         untung = untung + laba
     print("laba bulan ke",i,"sebesar ",laba)              ## Mencetak laba per bulan
     print("\ntotal laba adalah: ",untung)                 ## Menghitung total laba selama 8 bulan