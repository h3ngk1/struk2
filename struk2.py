# WARNET

Member = (str(input("Masukkan Tipe Member : ")))
Lama_Sewa = (int(input("Masukkan Lama Sewa (jam): ")))

Tarif_Reg = 3000
Tarif_VIP = 2000
Tarif_Paket_A = 10000
Tarif_Paket_B = 20000
Tarif_Paket_C = 30000

print(" ")
print(" ")
print('------------------Warnet_Abadi--------------------')
print("Jl. KS Tubun No. 1, Slipi, Palmerah, Jakarta Barat\n                ""Jangan Lupa Makan!!""            ")
import datetime
Sekarang = datetime.datetime.now()
print("Ingat Pulang, Waktu Sekarang : ", Sekarang.strftime("%H:%M, %d-%m-%Y"))
print('--------------------------------------------------')

if Member == "VIP" or Member == "vip" or Member == "v" or Member == "V":
    Biaya_Sewa = int(Lama_Sewa*Tarif_VIP)
elif Member == "Paket A" or Member == "a" or Member == "A" or Member == "PA" or Member == "pa":
    Biaya_Sewa = (Tarif_Paket_A)
elif Member == "Paket B" or Member == "b" or Member == "B" or Member == "PB" or Member == "pb":
    Biaya_Sewa = (Tarif_Paket_B)
elif Member == "Paket C" or Member == "c" or Member == "C" or Member == "PC" or Member == "pc":
    Biaya_Sewa = (Tarif_Paket_C)
else:
    Biaya_Sewa = int(Lama_Sewa*Tarif_Reg)

print("Tipe Member :", Member)
print("Lama Sewa : ", Lama_Sewa, "Jam")
print('--------------------------------------------------')
print("Biaya Sewa :", Biaya_Sewa)
print('--------------------------------------------------')
print("Tipe Member VIP adalah Layanan Membership Tahunan")
print("Tipe Member Reguler adalah member reguler tanpa langganan")
print("Tipe Member Paket A adalah member sekali beli, waktu sewa 5jam")
print("Tipe Member Paket B adalah member sekali beli, waktu sewa 10jam")
print("Tipe Member Paket C adalah member sekali beli, waktu sewa 15jam")
print('--------------------------------------------------')
print('--------------------------------------------------')
