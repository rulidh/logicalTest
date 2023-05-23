# Menampilkan Angka dari kelipatan 3 dan kelipatan 7, jika angka tersebut adalah kelipatan 3 dam 7, menampilkan huruf z

n= input("Banyak angka yang ditampilkan: ")
num= 0
numArray= []
x= len(numArray)
counter= 1

while(counter <= int(n)):
    num+= 1
    if(num% 3== 0 and num% 7== 0):
        numArray.append("Z")
        counter+= 1
    elif(num% 3== 0 or num% 7== 0):
        numArray.append(num)
        counter+= 1
    
print(numArray)
