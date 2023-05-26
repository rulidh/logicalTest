#Menampilkan Sandi yang tepat dengan aturan tertentu

checkNum= 0  #untuk cek tipe kata sandi
counter= 0

while True:                             #looping
    sandi= input("Input: ")
    x= len(sandi)                       #panjang sandi
    if x< 8 or x> 32:                   #kondisi aturan pertama, harus lebih dari 8 dan kurang dari 32
        print("Panjang sandi 8-32")     
    else:
        try:                   #menggunakan try except untuk menghiraukan error
            if(type(int(sandi[0]))== type(checkNum)):  #if statement untuk cek huruf pertama pada sandi angka/bukan
                print("Karakter awal tidak boleh angka")
        except ValueError:
            if any(char.isdigit() for char in sandi): #mengecek semua huruf pada sandi apakah ada angka/tidak
                
                #mengecek semua huruf pada sandi apakah ada huruf kecil dan besar
                if any(char.isupper() for char in sandi) and any(char.islower() for char in sandi):
                    print("Kata sandi valid")
                    break
                else:
                    print("Harus memiliki huruf kapital dan huruf kecil")
            else:
                print("Sandi harus memiliki angka")
                