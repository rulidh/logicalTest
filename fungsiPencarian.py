#Fungsi pencarian "sang gajah", "harimau", dan "serigala"

kalimat= input("Input: ")       #input
gajahCounter= 0                 #counter untuk gajah, serigala, dan harimau
serigalaCounter= 0
harimauCounter= 0

newKalimat= kalimat.upper()                                 #dibuat menjadi huruf kapital
newKalimat= newKalimat.replace(".", "")                     #menghilangkan titik
newKalimat= newKalimat.replace("SANG GAJAH", "SANGGAJAH")   #mengubah SANG GAJAH menjadi SANGGAJAH

newKalimat= newKalimat.split()   #mengubah tipe data menjadi array dan memasukkan ke array kata demi kata
for char in newKalimat:         #looping pada array
    if char== "SANGGAJAH":      #kondisi untuk menambah counter
        gajahCounter+= 1
    if char== "HARIMAU":
        harimauCounter+= 1
    if char== "SERIGALA":
        serigalaCounter+= 1
        
#menampilkan output yang diinginkan sesuai dengan counter yang didapatkan
print("sang gajah - " * gajahCounter + "serigala - " * serigalaCounter + "harimau - "* harimauCounter)


#contoh Input
#Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah.