import time;

waktu = time.asctime(time.localtime(time.time()))

print ("Waktu sekarang :", waktu)

print("Nama : Mochamad Akbar Fachrezy")
print("NIM  : 21120119120029")
print("Nama : Hafshah Quratta Ayun")
print("NIM  : 21120119120029")
print("Kelopok 9")
print("Shift : 1")
print("=== Program Pengecekan Pengiriman Barang ===")
def fungsi():
    print("Selamat Datang di Express Wonder")
fungsi()

print("Masukkan Nama Anda : ")
nama = input ("Nama : ")

print("Masukkan Password Anda : ")
Kunci = input ("Password : ")

if Kunci == "12345678" :


    while(True):
        print(" ===============SELAMAT DATANG DI APLIKASI PENGIRIMAN BAWANG===============")
        print("1. MENGIRIM BARANG")
        print("2. CEK PENGIRIMAN")
        print("0. Keluar")
        print("===========================================================")
        pil = int(input("Masukkan pilihan anda : "))
        if pil == 1:
            nama1 = input ("Nama Pengirim      : ")
            alamat1 = input ("Alamat Pengirim  : ")
            nama2 = input ("Nama Penerima      : ")
            alamat2 = input ("Alamat Penerima  : ")
            id_barang = input ("Id Barang     : ")
            print (" ========================== Cetak  ============================")
            print ("Nama Pengirim      : ",nama1,"\n","Alamat Pengirim  : ",alamat1,"\n","Nama Penerima      : ",nama2,"\n","Alamat Penerima  : ",alamat2,"\n"''"ID Barang  : ",id_barang)
        if pil == 2:
            print("masukkan id yang diterima")
            id = input ("ID Barang : ")
            if id == "12345678":
                while (True):
                    print("Nama Pengirim  : Akbar")
                    print("Alamat : Jalan CUmi Raya")
                    print("Barang Anda : HP")
                    print("Berat Barang  : 500 gram")
                    print("Nama Penerima : Taufik")
                    print("Alamat Penerima :Jalan Madu Manis")
                    break

            print("Terima Kasih Telah Menggunakan Aplikasi Kami")
        pilihan = input("Apakah Anda ingin mencoba lagi ? (Y/N) : ")
        if pilihan == "Y": continue
        if pilihan == "N": break
if Kunci != "12345678":
    print("Password Salah")
