# Fitur ATM yang disediakan:
# 1. Periksa PIN
# 2. Ganti PIN
# 3. Cek Saldo
# 4. Debet/Withdraw
# 5. Simpan/Deposit
# 6. Keluar
# 7. Cetak ringkasan transaksi

import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("\nSilahkan Masukkan PIN anda: "))
    trial = 0
    while (id != int(atm.checkPIN()) and trial < 3):
        if trial == 2:
            print("Terdapat Error. Silahkan ambil kartu anda, dan coba kembali.")
            exit()

        id = int(input("Pin Anda SALAH! Silahkan masukkan PIN lagi: "))
        trial += 1

    while True:
        print("----------------------------------------------")
        print("\nSelamat Datang di ATM Progate ...")
        print("Silahkan Pilih Menu yang tersedia ")
        print("\n 1 - Cek Saldo \n 2 - Debet/Penarikan \n 3 - Simpan \n 4 - Ganti PIN \n 5 - Keluar\n")
        selectedmenu = int(input("Masukkan nomor menu yang dipilih :.. "))
        
        while True:
            #Workflow Pilihan Menu 1
            if selectedmenu == 1:
                print("\nSaldo Anda Saat Ini : Rp. " + str(atm.checkBalance()) + "\n")
                break
            
            #Workflow Pilihan Menu 2
            elif selectedmenu == 2:
                nominal = int(input("\nMasukkan Jumlah Saldo yang akan didebet: "))
                verify_withdraw = input("Konfirmasi: Anda yakin akan melakukan debet dengan nominal Rp." + str(nominal) + " ? Y / N :.. ")
                if verify_withdraw == "y":
                    print("Saldo awal anda adalah: Rp. "+ str(atm.checkBalance()) + " ")
                elif verify_withdraw == "Y":
                    print("Saldo awal anda adalah: Rp. "+ str(atm.checkBalance()) + " ")
                elif verify_withdraw == "n":
                    print("Transaksi Dibatalkan.")
                    break
                elif verify_withdraw == "N":
                    print("Transaksi Dibatalkan.")
                    break
                else:
                    break
                
                if nominal % 50000 == 0:
                    if nominal + 50000 <= atm.checkBalance():
                        atm.withdrawBalance(nominal)
                        print("Transaksi Debet Anda Berhasil!")
                        print("Sisa Saldo Anda Saat Ini: Rp. "+ str(atm.checkBalance()) + " ")
                    else:
                        print("Maaf Saldo Anda Tidak Mencukupi.")
                        print("Silahkan Lakukan Penambahan Nominal Saldo.")
                elif nominal % 50000 != 0:
                    print("Maaf Nominal yang dimasukkan harus kelipatan Rp. 50.000")
                else:
                    print("Terjadi Kesalahan, Silahkan Ulangi.")
                    break
                break
           
            #Workflow Pilihan Menu 3
            elif selectedmenu == 3:
                nominal = int(input("Masukkan Nominal Saldo yang Akan Disimpan:.. "))
                verifiy_deposit = input("Konfirmasi: Apakah anda yakin untuk menyimpan dengan nominal Rp. " + str(nominal) + "? Y / N :.. ")

                if verifiy_deposit == "y":
                    if nominal % 50000 == 0:
                        atm.depositBalance(nominal)
                        print("Saldo Anda Sekarang Menjadi: Rp. " + str(atm.checkBalance()) + "\n")
                    else:
                        print("Jumlah Nominal harus kelipatan Rp. 50.000")
                        break
                elif verifiy_deposit == "Y":
                    if nominal % 50000 == 0:
                        atm.depositBalance(nominal)
                        print("Saldo Anda Sekarang Menjadi: Rp. " + str(atm.checkBalance()) + "\n")
                    else:
                        print("Jumlah Nominal harus kelipatan Rp. 50.000")
                        break
                elif verifiy_deposit == "n":
                    print("Transaksi Dibatalkan.")
                    break
                elif verifiy_deposit == "N":
                    print("Transaksi Dibatalkan.")
                    break                  
                else:
                    break
                break
            
            #Workflow Pilihan Menu 4
            elif selectedmenu == 4:
                verify_pin = int(input("Masukkan PIN Anda Saat Ini:.. "))
                pin_trial = 0
                while verify_pin != (int(atm.checkPIN()) and pin_trial < 3):
                    if verify_pin == int(atm.checkPIN()):
                        print("PIN yang Anda Masukkan Benar!\n")
                        break

                    if pin_trial == 2:
                        print("Silahkan Coba Lagi.\n")
                        exit()

                    verify_pin = int(input("PIN yang Anda Masukkan Salah! Silahkan Masukkan Lagi:.. "))
                    pin_trial += 1
                
                while True:
                    updated_pin = int(input("\nSilahkan Masukkan PIN yang Baru:.. "))
                    verify_newpin = int(input("Verifikasi: Silahkan Ketik Ulang PIN yang Baru:.. "))

                    if verify_newpin == updated_pin:
                        atm.pin = updated_pin
                        print("Verifikasi Berhasil! Nomor PIN Anda Telah diperbarui!")
                        break
                    else:
                        print("Verifikasi Tidak Berhasil, Silahkan Ulangi Lagi.")
                        break

                break
            
            #Workflow Pilihan Menu 5
            elif selectedmenu == 5:
                print("\n\nResi Tercetak Otomatis saat Anda Keluar. \n Harap Simpan Tanda Terima Ini \n Sebagai Bukti Transaksi")
                print("--------------------------")
                print("No. Rekord : " + str(random.randint(100000, 1000000)))
                print("Tanggal : " + str(datetime.datetime.now()))
                print("Saldo Saat Ini : Rp. " + str(atm.checkBalance()))
                print("---------------------------")
                print("Terima Kasih Telah Menggunakan Layanan ATM Progate!\nSemoga Hari Anda Menyenangkan.\n\n")
                quit()

            #Pilihan Menu Invalid
            else:
                print("Invalid: Masukan nomor menu anda salah! \n")
                break



