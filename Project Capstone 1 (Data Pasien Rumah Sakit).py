from tabulate import tabulate

# Data Awal
list_data_pasien = {
    "PS001": {
        "Nama": "Andi",
        "Umur": 30,
        "Jenis Kelamin": "Laki-laki",
        "Diagnosa": "Demam",
        "Ruangan" : "VVIP-001"
    },
    "PS002": {
        "Nama": "Dewi",
        "Umur": 12,  
        "Jenis Kelamin": "Perempuan",
        "Diagnosa": "Alergi Susu",
        "Ruangan": "Anak-020"
    },
    "PS003": {
        "Nama": "Siti",
        "Umur": 25,
        "Jenis Kelamin": "Perempuan",
        "Diagnosa": "Batuk",
        "Ruangan" : "Kelas 1-020"
    },
    "PS004": {
        "Nama": "Rudi",
        "Umur": 15,
        "Jenis Kelamin": "Laki-laki",
        "Diagnosa": "Asma",
        "Ruangan": "VIP-012"
    },
}

list_data_sampah = {}

# Pilihan Data untuk Form
list_kelamin = {
    1: "Laki-laki",
    2: "Perempuan"
}
list_diagnosa = {
    1: "Demam Berdarah",
    2: "Tifus",
    3: "Diabetes",
    4: "Hipertensi",
    5: "Asma",
    6: "Pneumonia",
    7: "Lainnya (isi Manual)"
}
list_ruangan = {
    1: "VVIP",
    2: "VIP",
    3: "Kelas 1",
    4: "Kelas 2",
    5: "Kelas 3",
    6: "Anak",
    7: "Isolasi",
    8: "ICU",
}

# Cek ID Pasien
def cek_id_pasien(sumber_list):
    while True:
        id_pasien = input("Masukkan ID Pasien: ").strip().upper()
        if id_pasien in sumber_list:
            return id_pasien  # Mengembalikan ID yang valid
        else:
            print("ID Pasien Tidak Ditemukan! Silahkan Masukkan Lagi\n")


# Input Form Pasien
def input_form_data_pasien():
    
    print("\nSilahkan Masukkan Data")
    
    # Input Nama
    while True:
        nama_pasien = input("Masukkan Nama Pasien: ").strip().title()
        if nama_pasien:
            break
        else:
            print("-- Nama Pasien Tidak Boleh Kosong! --")

    # Input Angka
    while True:
        try:
            umur_pasien = int(input("\nMasukkan Umur Pasien: ").strip())
            if 0 <= umur_pasien < 160:
                break
            else:    
                print("-- Umur Tidak Boleh Kurang dari 0 dan Lebih dari 180 Tahun! --")
        except ValueError:
            print("-- Umur Harus Angka! --")
  
    ## Input Pilih Jenis Kelamin
    print("\nPilih Jenis Kelamin")
    # Menampilkan daftar key dan value dict di list_kelamin
    for angka, kelamin in list_kelamin.items():
        print(f"{angka}. {kelamin}")
        
    while True:
        try:
            pilih_jenis_kelamin = int(input("Pilih Jenis Kelamin (1/2): "))
            if pilih_jenis_kelamin in list_kelamin:
                # Ambil Value dalam list_kelamin dan disimpan di jenis_kelamin
                jenis_kelamin = list_kelamin[pilih_jenis_kelamin]
                break
            else:
                print("-- Pilihan tidak valid! Masukkan 1 atau 2 --")
        except ValueError:
            print("-- Input Harus Angka dan Tidak Boleh Kosong! --")            

    ## Input Pilih Diagnosa
    print("\nPilih Diagnosa")
    for angka, diagnosa in list_diagnosa.items():
        print(f"{angka}. {diagnosa}")
        
    while True:
        try:
            pilih_diagnosa = int(input("Pilih Diagnosa Pasien (1-7): "))
            if pilih_diagnosa in list_diagnosa:
                if pilih_diagnosa == 7:
                    diagnosa_pasien = input("Masukkan Diagnosa Lainnya: ").strip()
                    if not diagnosa_pasien:
                        print("-- Diagnosa Pasien Tidak Boleh Kosong! --")
                        continue
                else:
                    diagnosa_pasien = list_diagnosa[pilih_diagnosa]
                break
            print("-- Pilihan hanya 1-7! --")
        except ValueError:
            print("-- Input Harus Angka dan Tidak Boleh Kosong! --")

    ## Input Pilih Ruangan
    print("\nPilih Ruangan")
    for angka, ruangan in list_ruangan.items():
        print(f"{angka}. {ruangan}")
    
    while True:
        try:
            pilih_ruangan = int(input("Pilih Ruangan Pasien (1-8): "))
            if pilih_ruangan in list_ruangan:
                while True:
                    try:
                        no_kamar = int(input("\nMasukkan Nomor Kamar: "))
                        ruangan_pasien = (f"{list_ruangan[pilih_ruangan]}-{no_kamar:03}")
                        print()
                        break
                    except ValueError:
                        print("-- Nomor Kamar Harus Angka dan Tidak Boleh Kosong! --")
                break
            else:
                print("-- Pilih Hanya (1-8)! --")
        except ValueError:
            print("-- Input Harus Angka dan Tidak Boleh Kosong! --")
    
    return {
        "Nama"          : nama_pasien,
        "Umur"          : umur_pasien,
        "Jenis Kelamin" : jenis_kelamin,
        "Diagnosa"      : diagnosa_pasien,
        "Ruangan"       : ruangan_pasien
    }

# Menampilkan Data Konfirmasi Pasien
def tampilkan_data_konfirmasi(id_pasien, data):
    print(f"ID Pasien      : {id_pasien}")
    for key, value in data.items():
        print(f"{key:<15}: {value}")

# Menu 1
## Menampilkan Data Pasien 
def lihat_data_pasien():
    print("\n" + "="*33 + " DATA PASIEN " + "="*33)
    
    tabel_data_pasien = []
    
    for id_pasien, data in list_data_pasien.items():
        # Membuat 1 baris data pasien
        row = [
            id_pasien,
            data["Nama"],
            data["Umur"],
            data["Jenis Kelamin"],
            data["Diagnosa"],
            data["Ruangan"]
        ]
         # Menambahkan baris ke dalam tabel
        tabel_data_pasien.append(row)
        
    # Menampilkan tabel dengan format grid    
    print(tabulate(tabel_data_pasien, headers=["ID Pasien","Nama","Umur","Jenis Kelamin","Diagnosa","Ruangan"], tablefmt= "simple_grid"))
    print("="*79)

# Menu 1
## Mencari Data Pasien
def cari_data_pasien():
    
    print("\n==- Cari Data Pasien -==")    
    cari_pasien = input("Masukkan ID atau Nama Pasien: ").strip()

    hasil_temuan = []
    
    # Mencari ID dan Nama dengan looping
    for id_pasien, data in list_data_pasien.items():
        if cari_pasien.upper() == id_pasien or cari_pasien.title() == data['Nama']:
            
            hasil_temuan.append([
            id_pasien,
            data["Nama"],
            data["Umur"],
            data["Jenis Kelamin"],
            data["Diagnosa"],
            data["Ruangan"]
        ])
            
    # Menampilkan Hasil
    # Tampilkan hasil
    if hasil_temuan:
        print("\n" + "="*25 + " HASIL PENCARIAN DATA PASIEN " + "="*25)
        print(tabulate(
            hasil_temuan,
            headers=["ID Pasien", "Nama", "Umur", "Jenis Kelamin", "Diagnosa", "Ruangan"],
            tablefmt="simple_grid"))
        print("="*79)
    else:
        print("\n -- Data Tidak Ditemukan! --")

# Menu 1
## Filtering Data Pasien 
def filter_Umur_pasien():
    print("\n==- Filter Umur Pasien -==")
    print("1. Pasien Dewasa (Umur 17 Tahun ke atas)")
    print("2. Pasien Anak-anak (Umur di bawah 17 Tahun)")
    
    try:
        pilihan = int(input("\nPilih Kategori Umur (1-2): "))
        if pilihan not in [1, 2]:
            print("\n-- Pilihan hanya boleh 1 (Dewasa) atau 2 (Anak-anak)! --")
            return
            
        hasil_filter = []
        
        # Filter data berdasarkan pilihan
        for id_pasien, data in list_data_pasien.items():
            if (pilihan == 1 and data['Umur'] >= 17) or (pilihan == 2 and data['Umur'] < 17):
                hasil_filter.append([
                    id_pasien,
                    data["Nama"],
                    data["Umur"],
                    data["Jenis Kelamin"],
                    data["Diagnosa"],
                    data["Ruangan"]
                ])
        
        # Tampilkan hasil
        if hasil_filter:
            print("\n" + "="*25 + " HASIL DATA PASIEN " + "="*25)
            print(tabulate(
                hasil_filter,
                headers=["ID Pasien", "Nama", "Umur", "Jenis Kelamin", "Diagnosa", "Ruangan"],
                tablefmt="simple_grid"
            ))
            print("="*79)
        else:
            print("\n-- Tidak ada pasien yang sesuai dengan kriteria ini --")
            
    except ValueError:
        print("\n-- Input harus berupa angka (1-2)! --")
        
# Menu 2
## Menambah Data Pasien
def tambah_data_pasien():
    
    # Input Data Pasien Terlebih Dahulu
    id_pasien = (f"PS{len(list_data_pasien) + 1:003}")
    
    # Data Pasien
    data_pasien = input_form_data_pasien()
    
    # Tampilkan Data Sebelum Konfirmasi
    print("\nData Pasien yang akan Disimpan: ")
    tampilkan_data_konfirmasi(id_pasien, data_pasien)

    # Konfirmasi Penyimpanan
    while True:
        konfirmasi = input("\nApakah Anda Ingin Menambahkan Pasien ini? (y/t): ").lower()
        if konfirmasi == 'y':
            
            # Tambah Data Pasien Dictionary
            list_data_pasien[id_pasien] = data_pasien
            print(f"\n-- Data Pasien {id_pasien} Berhasil Ditambahkan! --")
            lihat_data_pasien()
            break
        elif konfirmasi == 't':
            print("\n-- Data Pasien Tidak Disimpan --")
            break
        else:
            print("\n-- Input salah! Masukkan 'y' atau 't'! --")  

# Menu 3
## 3.Mengubah Data Pasien 
def ubah_data_pasien():
    lihat_data_pasien()
    
    
    # Cek Data Pasien
    id_pasien = cek_id_pasien(list_data_pasien)
    
    # Data diubah
    data_ubah = input_form_data_pasien()
    
    # Tampilkan Data Sebelum Konfirmasi
    print("Data Pasien yang akan Diubah: ") 
    tampilkan_data_konfirmasi(id_pasien, data_ubah)

    # Konfirmasi Pengubahan
    while True:
        konfirmasi = input(f"\nApakah Anda ingin Mengubah Data {id_pasien}? (y/t):").lower()
        if konfirmasi == 'y':
            list_data_pasien[id_pasien] = data_ubah
            print(f"\nData Pasien {id_pasien} Berhasil Diubah!")
            lihat_data_pasien()
            break
        elif konfirmasi == 't':
            print("\n-- Perubahan Data Dibatalkan --\n")
            break
        else:
            print("\n-- Input salah! Masukkan 'y' atau 't'! --\n")

# Menu 4
## Menu Hapus
### 1.Menghapus Data Pasien
def hapus_data_pasien():
    lihat_data_pasien()

    # Cek Data Pasien
    id_pasien = cek_id_pasien(list_data_pasien)
    
    # Tampilkan Data Sebelum Dihapus
    tampilkan_data_konfirmasi(id_pasien, list_data_pasien[id_pasien])

    # Konfirmasi
    while True:
        konfirmasi = input(f"Apakah Data Pasien {id_pasien} ingin Dihapus? (y/t):  ").lower()
        if konfirmasi == 'y':
            # Pindahkan ke List Sampah
            list_data_sampah[id_pasien] = list_data_pasien[id_pasien]
            del list_data_pasien[id_pasien]
            print(f"\n-- Data Pasien {id_pasien} Telah Dihapus! --")
            lihat_data_pasien()
            break
        elif konfirmasi == 't':
            print("-- Penghapusan Data Dibatalkan --\n")
            break
        else:
            print("\n --Input salah! Masukkan 'y' atau 't'! --\n") 

# Menu 4
## Menu Hapus
### 2.Menampilkan Data Pasien yang Dihapus  
def lihat_data_sampah():
    
    print("="*30 + " Data Pasien Dihapus " + "="*30)
    
    tabel_data_sampah = []
    
    for id_pasien, data in list_data_sampah.items():
        row = [
            id_pasien,
            data["Nama"],
            data["Umur"],
            data["Jenis Kelamin"],
            data["Diagnosa"],
            data["Ruangan"]
        ]
        
        tabel_data_sampah.append(row)
        
    print(tabulate(tabel_data_sampah, headers=["ID Pasien","Nama","Umur","Jenis Kelamin","Diagnosa","Ruangan"], tablefmt= "simple_grid"))

# Menu 4
## Menu Hapus
### 3. Memulihkan data pasien          
def pulihkan_data():
    
    # Cek jika list sampah kosong
    if not list_data_sampah:
        print("\n-- Tidak ada data pasien yang dihapus! --\n")
        return
    
    lihat_data_sampah()
    
    # Periksa Data pada list sampah
    id_pasien = cek_id_pasien(list_data_sampah)
    
    # Tampilkan Data Sebelum Konfirmasi
    print("\nData Pasien yang akan Disimpan: ")
    tampilkan_data_konfirmasi(id_pasien, list_data_sampah[id_pasien])
    
    # Konfirmasi
    while True:
        konfirmasi = input(f"Apakah Data Pasien {id_pasien} ingin Dipulihkan? (y/t): ").lower()
        if konfirmasi == 'y':
            list_data_pasien[id_pasien] = list_data_sampah.pop(id_pasien)
            print(f"\nData {id_pasien} berhasil dipulihkan!\n")
            break
        elif konfirmasi == 't':
            print("-- Pemulihan Data Dibatalkan --\n")
            break
        else:
            print("\n-- Input salah! Masukkan 'y' atau 't'! --\n")
                         
#** Menampilkan Menu Lihat Data
def menu_lihat():
    while True:
        print("\n" + "="*5 + " MENU LIHAT " + "="*5)
        
        print("1. Lihat Data Pasien")
        print("2. Cari Data Pasien")
        print("3. Filter Umur Pasien")
        print("4. Kembali ke Menu Utama")
        
        print("=" * 25 + "\n")
        
        try:
            pilih_menu_lihat = int(input("Silahkan Pilih Menu (1-4): "))
            
            match pilih_menu_lihat:
                case 1 : lihat_data_pasien()
                case 2 : cari_data_pasien()
                case 3 : filter_Umur_pasien()
                case 4 : 
                    return 
                case _ : 
                    print("\n-- Input Tidak Valid! Silahkan Pilih (1-4) -- ")
                    continue
            selesai = input("\nApakah Selesai di Menu Lihat? (y/t) ").lower()
            if selesai == 'y':
                break                              
        except ValueError:
            print("-- Input Harus Angka! --")

#** Menampilkan Menu Tambah Data
def menu_tambah():
    while True:
        print("\n" + "="*5 + " MENU TAMBAH " + "="*5)
        
        print("1. Tambah Data Pasien")
        print("2. Kembali ke Menu Utama")
        
        print("=" * 25 + "\n")
        
        try:
            pilih_menu_tambah = int(input("Silahkan Pilih Menu (1-2): "))
            
            match pilih_menu_tambah:
                case 1 : tambah_data_pasien()
                case 2 : 
                    return 
                case _ : 
                    print("\n-- Input Tidak Valid! Silahkan Pilih (1-2) -- ")
                    continue
            selesai = input("\nApakah Selesai di Menu Tambah? (y/t) ").lower()
            if selesai == 'y':
                break                              
        except ValueError:
            print("-- Input Harus Angka! --")
            
#** Menampilkan Menu Ubah Data
def menu_ubah():
    while True:
        print("\n" + "="*5 + " MENU UBAH " + "="*5)
        
        print("1. Ubah Data Pasien")
        print("2. Kembali ke Menu Utama")
        
        print("=" * 25 + "\n")
        
        try:
            pilih_menu_tambah = int(input("Silahkan Pilih Menu (1-2): "))
            
            match pilih_menu_tambah:
                case 1 : ubah_data_pasien()
                case 2 : 
                    return 
                case _ : 
                    print("\n-- Input Tidak Valid! Silahkan Pilih (1-2) -- ")
                    continue
            selesai = input("\nApakah Selesai di Menu Ubah? (y/t) ").lower()
            if selesai == 'y':
                break                              
        except ValueError:
            print("-- Input Harus Angka! --")
                        
#** Menampilkan Menu Hapus Pasien
def menu_hapus():
    
    while True:
        print("\n" + "="*5 + " MENU HAPUS " + "="*5)
        
        print("1. Hapus Data Pasien")
        print("2. Lihat Data Pasien Dihapus")
        print("3. Pulihkan Data Pasien")
        print("4. Kembali ke Menu Utama")
        
        print("=" * 25 + "\n")
        
        try:
            pilih_menu_hapus = int(input("Silahkan Pilih Menu (1-4): "))
            
            match pilih_menu_hapus:
                case 1 : hapus_data_pasien()
                case 2 : lihat_data_sampah()
                case 3 : pulihkan_data()
                case 4 : 
                    return 
                case _ : 
                    print("\n-- Input Tidak Valid! Silahkan Pilih (1-4) --")
                    continue
            selesai = input("Apakah Selesai di Menu Hapus? (y/t): ").lower()
            if selesai == 'y':
                break                                       
        except ValueError:
            print("-- Input Harus Angka! --")
            
#* Menampilkan Menu Data Pasien Rumah Sakit
def main():
    while True:
        print("\n"+"="*10 + " MENU DATA PASIEN RUMAH SAKIT " + "="*10)
        
        print("1. Menu Melihat Data Pasien Rumah Sakit")
        print("2. Menu Menambahkan Data Pasien Rumah Sakit")
        print("3. Menu Mengubah Data Pasien Rumah Sakit")
        print("4. Menu Menghapus Data Pasien Rumah Sakit")
        print("5. Keluar")
        
        print("=" * 50 + "\n")
        
        try:
            pilih_menu = int(input("Silahkan Pilih Menu 1-5: "))
            
            match pilih_menu:
                case 1 : menu_lihat()
                case 2 : menu_tambah()
                case 3 : menu_ubah()
                case 4 : menu_hapus()
                    
                case 5 :
                    print("Terima Kasih!")
                    break
                case _:
                    print("\n-- Pilihan Tidak Valid! Silahkan Pilih (1-5) --")
            # Tanya Selesai Program
            if pilih_menu in []:
                selesai = input("\nApakah Selesai? (y/t): ").lower()
                if selesai == 'y':
                    print("Terima Kasih!")
                    break

        except ValueError:
            print("\n-- Input Harus Angka! --")
            
    return print("Program Selesai!")

main()