checkNum= 0
counter= 0

while True:
    sandi= input("Input: ")
    x= len(sandi)
    if x< 8 or x> 32:
        print("Panjang sandi 8-32")
    else:
        try:
            if(type(int(sandi[0]))== type(checkNum)):
                print("Karakter awal tidak boleh angka")
        except ValueError:
            if any(char.isdigit() for char in sandi):
                if any(char.isupper() for char in sandi) and any(char.islower() for char in sandi):
                    print("Kata sandi valid")
                else:
                    print("Harus memiliki huruf kapital dan huruf kecil")
            else:
                print("Sandi harus memiliki angka")
                