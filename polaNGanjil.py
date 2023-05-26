#Menampilkan pola yang diberikan jika N adalah angka ganjil

#Menampilkan pola tertentu dengan input angka ganjil

#input
n = int(input("Input angka: "))

#kondisi apakah inputan ganjil atau tidak
if n%2 == 1:
    #looping
    for i in range(n):
        for j in range(n):
            #untuk mengecek apakah yang harus ditampilkan X atau O
            if i== 0 or i== n- 1 or j== 0 or j== n- 1 or i== j or i== n- 1- j:
                print("X", end="")
            else:
                print("O", end="")
        print()
else:
    print("Harus bilangan ganjil")
    