kalimat= input("Input: ")
gajahCounter= 0
serigalaCounter= 0
harimauCounter= 0

newKalimat= kalimat.upper()
newKalimat= newKalimat.replace(".", "")
newKalimat= newKalimat.replace("SANG GAJAH", "SANGGAJAH")

newKalimat= newKalimat.split()
for char in newKalimat:
    if char== "SANGGAJAH":
        gajahCounter+= 1
    if char== "HARIMAU":
        harimauCounter+= 1
    if char== "SERIGALA":
        serigalaCounter+= 1
        
print("sang gajah - " * gajahCounter + "serigala - " * serigalaCounter + "harimau - "* harimauCounter)

#Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah.