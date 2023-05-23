# Menampilkan Angka dari kelipatan 3 dan kelipatan 7, jika angka tersebut adalah kelipatan 3 dam 7, menampilkan huruf z

n= input("Banyak angka yang ditampilkan: ") #input banyaknya deretan angka yang diinginkan
num= 0                                      
numArray= []
x= len(numArray)                            #panjang dari array
counter= 1                                  #penanda

while(counter <= int(n)):                   #dihentikan jika nilai counter lebih dari nilai n
    num+= 1                                 #angka yang dicek kelipatannya
    if(num% 3== 0 and num% 7== 0):          #jika sama sama kelipatan 3 dan 7, tambahkan nilai Z
        numArray.append("Z")
        counter+= 1
    elif(num% 3== 0 or num% 7== 0):         #jika salah satunya, tambahkan angka yang ditest
        numArray.append(num)
        counter+= 1
    
print(numArray)                           
