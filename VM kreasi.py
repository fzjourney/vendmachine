#Description : Vending Machine Program (Indonesia)

import time;import random;import sys;
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)

print("####### SELAMAT DATANG DI VENDING MACHINE #######")

print("\r");print("Silahkan masukkan jumlah uang (Dalam Rupiah)")

itung = []
berhenti = False

while (not berhenti):
    uang =int(input("Masukkan uang: "))
    itung.append(uang)
    yesorno=input("Masukkan uang lagi? Yes/No: ")
    if (yesorno=="No")or(yesorno=="no"):
        berhenti = True

uang_masuk = sum(itung)

print("\r");mengetik("Tunggu sebentar ^_^ . . .")
time.sleep(3)
print("\r")

#List harga
m1 =5000 ; M1 = 7500
m2 =3500 ; M2 = 6000
m3 =3000 ; M3 = 10000
m4 =4000 ; M4 = 12500
m5 =4000 ; M5 = 15000

print("################### MENU LIST ###################")
print(">>>>> SALDO: Rp"+str(uang_masuk)+" <<<<<")
print("~~~Minuman~~~")
print("1. Nutriboost (Rp5.000)")
print("2. Fruit Tea  (Rp3.500)")
print("3. Teh Pucuk  (Rp3.000)")
print("4. Fanta      (Rp4.000)")
print("5. Sprite     (Rp4.000)")
print("~~~Makanan~~~")
print("1. Chitato    (Rp7.500)")
print("2. Lays       (Rp6.000)")
print("3. Doritos    (Rp10.000)")
print("4. Tango      (Rp12.500)")
print("5. Pocky      (Rp15.000)")

def kembalian():
    kembalian = total
    print("\r");mengetik("Tunggu sebentar untuk proses . . .")
    time.sleep(2)
    print("\r");print("Selamat Dinikmati "+str(produk)+"nya")
    print("Kembalian: Rp"+str(kembalian))
    
print("\r");print("Pilih menu dengan cara ketikan nama produk")
print("!!! Tuliskan sesuai pada menu !!!")    
pilih = input("Masukkan produk: ")

while (pilih):
    if (pilih=="Nutriboost")or(pilih=="Fruit Tea")or(pilih=="Teh Pucuk")or(pilih=="Fanta")or(pilih=="Sprite"):
        print("\r");print("Ingin yang dingin atau biasa?")
        suhu = input("Ketik disini: ")
        if (suhu=="dingin")or(suhu=="es")or(suhu=="cold"):
            produk = (pilih.title()+" Dingin")
            if (pilih=="Nutriboost"):
                biaya = m1
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
            elif (pilih=="Fruit Tea"):
                biaya = m2
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
            elif (pilih=="Teh Pucuk"):
                biaya = m3
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
            elif (pilih=="Fanta"):
                biaya = m4
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
            elif (pilih=="Sprite"):
                biaya = m5
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
        elif (suhu =="biasa"):
            produk = (pilih.title()+" Biasa")
            if (pilih=="Nutriboost"):
                biaya = m1
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    print("\r");kembalian() ; break
            elif (pilih=="Fruit Tea"):
                biaya = m2
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
            elif (pilih=="Teh Pucuk"):
                biaya = m3
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
            elif (pilih=="Fanta"):
                biaya = m4
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
            elif (pilih=="Sprite"):
                biaya = m5
                total = uang_masuk - biaya
                if (total<0):
                    print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                    pilih = input("Masukkan produk: ")
                else :
                    kembalian() ; break
        else :  
            "Ketik hanya dengan huruf kecil"
    elif (pilih=="Chitato")or(pilih=="Lays")or(pilih=="Doritos")or(pilih=="Tango")or(pilih=="Pocky"):
        produk = (pilih.title())
        if (pilih=="Chitato"):
            biaya = M1
            total = uang_masuk - biaya
            if (total<0):
                print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                pilih = input("Masukkan produk: ")
            else :
                kembalian() ; break
        elif (pilih=="Lays"):
            biaya = M2
            total = uang_masuk - biaya
            if (total<0):
                print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                pilih = input("Masukkan produk: ")
            else :
                kembalian() ; break
        elif (pilih=="Doritos"):
            biaya = M3
            total = uang_masuk - biaya
            if (total<0):
                print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                pilih = input("Masukkan produk: ")
            else :
                kembalian() ; break
        elif (pilih=="Tango"):
            biaya = M4
            total = uang_masuk - biaya
            if (total<0):
                print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                pilih = input("Masukkan produk: ")
            else :
                kembalian() ; break
        elif (pilih=="Pocky"):
            biaya = M5
            total = uang_masuk - biaya
            if (total<0):
                print("\r");print("Uang yang digunakan kurang silahkan pilih yang lain")
                pilih = input("Masukkan produk: ")
            else :
                kembalian() ; break
    else:
        print("\r");print("Ketik sesuai pada Display (Beserta kapitalnya)")   
        pilih = input("Masukkan produk: ")

print("\r")
print("################## TERIMA KASIH ##################")