# labspy03
# Source code
	n=int(input("Masukkan Nilai N: ")) ## Memperkenalkan variable n sebagai integer, kemudian menginputkan nilainya
	
	from random import random ## Mengimport fungsi random a=random() ## Memperkenalkan variale a sebagai random

	jumlah=n+1 ## Jumlah = varible n + 1 start=1 ## Dimulai dari angka 1 stop=jumlah ## Berhenti ketika variable jumlah sudah sesuai step=1 ## Step angka 1

	for i in range(start,stop,step): ## Perulangan i dengan nilai awal variable start, nilai akhir variable stop dan step variable step print("data ke : ",i,"=",(a)) ## Mencetak hasil print("\nDone")