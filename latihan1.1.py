n=int(input("masukan nilai N: "))           ## Memperkenalkan variable n sebagai integer, kemudian menginputkan nilainya

from random import random                   ## Mengimport fungsi random
a=random()                                  ## Memperkenalkan variable a sebagai random

jumlah=n+1                                  ## Jumlah = variabel n+1
start=1                                     ## Dimulai dari angka 1
stop=jumlah                                 ## Berhenti ketika jumlah variabel sudah sesuai
step=1                                      ## Step angka 1

for i in range(start,stop,step):            ## Perulangan i dengan nilai awal variabel start, nilai akhir variabel stop dan step variabel step
    print("data ke : ",i,"=",(a))           ## Mencetak hasil
print("\nDone")