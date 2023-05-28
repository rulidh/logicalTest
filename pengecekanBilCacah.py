#cek bilangan cacah terkecil dari contoh array yang tersedia

arrNum= [2, 3, 4, 6]       #Inisialisasi array
arrNum.sort()               #Mengurutkan array
num= arrNum[0]              #inisialisasi number agar sama dengan index pertama array

for i in arrNum:            #looping semua angka dari array
    if num!= i:             #kondisi jika num tidak sama dengan i
        print(num)
        break
    num+= 1                 #increment
    
        
        
        