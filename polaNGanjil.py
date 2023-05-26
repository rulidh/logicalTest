#Menampilkan pola yang diberikan jika N adalah angka ganjil

n = int(input("Input angka: "))

if n%2 == 1:
    for i in range(n):
        for j in range(n):
            if i== 0 or i== n- 1 or j== 0 or j== n- 1 or i== j or i== n- 1- j:
                print("X", end="")
            else:
                print("O", end="")
        print()
else:
    print("Harus bilangan ganjil")
    