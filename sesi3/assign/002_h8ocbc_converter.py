#Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin
def kelvinCelcius(drjt, pilih):
    if pilih == 1:
        return drjt + 273.15 # celcius ke Kelvin (0 °C + 273,15 = 273,15 K)
    elif pilih == 2:
        return drjt - 273.15 # Kelvin ke celcius (0 K − 273,15 = -273,1 °C)

#Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit.
#Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin.
# Panggil function yang pertama jika diperlukan.
def keFarenheit(drjt, pilih):
    if pilih == 1:
        return f"{((drjt*9)/5)+32}" #celcius ke farenheit ((0 °C × 9/5) + 32 = 32 °F)
    elif pilih == 2:
        return f"{((kelvinCelcius(drjt,2)*9)/5)+32}" #kelvin ke farenheit ((0 K − 273,15) × 9/5 + 32 = -459,7 °F)

#Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit.
#Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin.
def dariFarenheit(drjt, pilih):
    if pilih == 1:
        return f"{(5/9)*(drjt-32)}" #farenheit ke celcius ((0 °F − 32) × 5/9 = -17,78 °C)
    elif pilih == 2:
        return f"{kelvinCelcius((5/9)*(drjt-32),1)}" #farenheit ke kelvin ((0 °F − 32) × 5/9 + 273,15 = 255,372 K)

print("Tugas 2_FSDO002ONL002_WIDYAWATI NUR SHOLIKHAH")
i=0
while i==0:
    lagi=int(input("Hitung? (1 = ya & 0 = tidak ) = "))
    
    if(lagi==1):
        suhu = input("\nMasukan suhu? (Misal: 30C, 20F, 21K): ") 
        drjt = int(suhu[:-1])
        inputan = suhu[-1]
        if inputan.upper() == "C":
            pilih = int(input("1 = Kelvin, 2 = Farenheit, 3 = Kelvin dan Farenheit   "))
            if pilih == 1:
                #Celcius ke Kelvin
                print(f"{drjt} Celcius = {kelvinCelcius(drjt,1)} Kelvin")
            elif pilih == 2:
                #Celcius ke Farenheit
                print(f"{drjt} Celcius = {keFarenheit(drjt,1)} Farenheit")
            elif pilih == 3:
                #Celcius ke Kelvin
                print(f"{drjt} Celcius = {kelvinCelcius(drjt,1)} Kelvin")
                #Celcius ke Farenheit
                print(f" {drjt} Celcius = {keFarenheit(drjt,1)} Farenheit")
            else:
                print("Masukan Salah")

        elif inputan.upper() == "K":
            pilih = int(input("1 = celcius, 2 = Farenheit, 3 = celcius dan Farenheit   "))
            if pilih == 1:
                #Kelvin ke Celcius
                print(f" {drjt} Kelvin = {kelvinCelcius(drjt,2)} Celcius")
            elif pilih == 2:
                #Kelvin ke Farenheit
                print(f" {drjt} Kelvin = {keFarenheit(drjt,2)} Farenheit")
            elif pilih == 3:
                #Kelvin ke Celcius
                print(f" {drjt} Kelvin = {kelvinCelcius(drjt,2)} Celcius")
                #Kelvin ke Farenheit
                print(f" {drjt} Kelvin = {keFarenheit(drjt,2)} Farenheit")
            else:
                print("Masukan Salah")

        elif inputan.upper() == "F":
            pilih = int(input("1 = celcius, 2 = kelvin, 3 = celcius dan kelvin   "))
            if pilih == 1:
                #Farenheit ke Celcius
                print(f"{drjt} Farenheit ={dariFarenheit(drjt,1)} Celcius")
            elif pilih == 2:
                #Farenheit ke Kelvin
                print(f"{drjt} Farenheit = {dariFarenheit(drjt,2)} Kelvin")
            elif pilih == 3:
                #Farenheit ke Celcius
                print(f"{drjt} Farenheit = {dariFarenheit(drjt,1)} Celcius")
                #Farenheit ke Kelvin
                print(f"{drjt} Farenheit = {dariFarenheit(drjt,2)} Kelvin")
            else:
                print("Masukan Salah")
        else:
            print('inputan salah')
    elif(lagi!=1):
        print("anda keluar")
        i=1