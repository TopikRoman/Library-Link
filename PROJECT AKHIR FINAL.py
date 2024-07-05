import os                                   
from datetime import datetime, timedelta    
import csv                                 
import pandas as pd                         
from tabulate import tabulate               

def LaunchPage():
    os.system("cls") 
           
    print(f"""
#======================================================================# 
#                     _      __ __  _      ____                        #
#                    | |    |  |  || |    |    |                       #
#                    | |    |  |  || |     |  |                        #
#                    | |___ |  ~  || |___  |  |                        #
#                    |     ||___, ||     | |  |                        #
#                    |     ||     ||     | |  |                        #
#                    |_____||____/ |_____||____|                       #
#                                                                      #
#======================================================================#
#                |                                |                    #
#                |         SELAMAT DATANG         |                    #
#                |                                |                    #
#---------------+++------------------------------+++-------------------#
#                |    Tekan Enter Untuk Lanjut    |                    #
#======================================================================#""")
    input("")
    Login()

#LAUNCH PAGE SELESAI

# FITUR LOGIN

def Login():
    """Bagian ini akan mengambil data dari file DataAdmin.csv untuk melakukan pengecekan terhadap username dan password yang dimasukkan"""
    os.system("cls") 
    print(f"""#{"="*70}#\n#{"LOGIN PAGE".center(70)}#\n#{"-"*70}#\n#{"MASUKKAN USERNAME & PASSWORD".center(70)}#\n#{"="*70}#""")
    
    UsernameSuperAdmin = "SuperAdmin" 
    PasswordSuperAdmin = "SuperAdmin" 
        
    UsernameInput = input("Username : ") 
    PasswordInput = input("Password : ") 
    
    if UsernameInput == UsernameSuperAdmin and PasswordInput == PasswordSuperAdmin: 
        print(f"""#{'='*70}#\n#{"LOGIN BERHASIL".center(70)}#\n#{'-'*70}#\n#{"SELAMAT DATANG SUPER ADMIN".center(70)}#\n#{'='*70}#""")
        input("")
        os.system("cls") 
        TampilanMenuSuperAdmin() 
    elif UsernameInput != UsernameSuperAdmin and PasswordInput != PasswordSuperAdmin: 
        CekFileAdminLogin = os.path.isfile("DataAdmin.csv") 
        if CekFileAdminLogin == True:
            with open("DataAdmin.csv", "r") as BukaDataAdmin: 
                CekUsn = csv.reader(BukaDataAdmin) 
                next(CekUsn)  
                for row in CekUsn: 
                    if row[0] == UsernameInput and row[1] == PasswordInput: 
                        print(f"""#{'='*70}#\n#{'LOGIN BERHASIL'.center(70)}#\n#{'-'*70}#\n#{f'SELAMAT DATANG {row[2].upper()}'.center(70)}#\n#{'='*70}#""")
                        input("")
                        TampilanMenuAdmin()
                        break
                    else:
                        print("Username/Password yang anda masukkan salah")
                        input("")
                        Login() 
        elif CekFileAdminLogin == False: 
            print("Mohon Maaf Data Belum Ada")
            input("")
            Login() 
    else:
        Login()

# ------------------------------------------------------SEMUA TENTANG BUKU------------------------------------------------------ #

# MENAMBAH BUKU
def MenambahkanDataBuku():
    """Bagian ini akan meminta pengguna untuk memasukkan Judul, penulis, tahun terbit dan kategori buku yang selanjutnya akan dimasukkan kedalam file DaftarBuku.CSV"""
    os.system("cls")
    print(f'''#{'='*70}#\n#{"MENAMBAHKAN DATA BUKU".center(70)}#\n#{"-"*70}#\n#{"SILAHKAN MASUKKAN DATA BUKU".center(70)}#\n#{"="*70}#''')
    JudulBuku = input("Judul Buku   : ")  
    Penulis = input("Penulis Buku : ")       
    TahunTerbit = input("Tahun Terbit : ")           
    Kategori = input("Kategori     : ")
    JumlahBuku = input("Jumlah Buku  : ")
    
    if len(JudulBuku) < 2 or len(Penulis) < 2 or len(TahunTerbit) < 4  or len(Kategori) < 2 or len(JumlahBuku) == 0 or JumlahBuku.isdigit() == False or TahunTerbit.isdigit() == False or JumlahBuku == "0":
        print("Mohon Maaf Data Kurang Lengkap/Tidak Sesuai")
        print("Mohon Masukkan Data Kembali")
        input("")
        TampilanMenuAdmin()
    else: 
        Keputusan = input("Tekan [Y] Untuk Menyimpan Data, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu : ").upper()
        if Keputusan == "Y":
            CekFileDaftarBuku = os.path.isfile("DaftarBuku.csv") 
            with open("DaftarBuku.csv", "a", newline='') as BukaDaftarBuku: 
                TulisDaftarBuku = csv.writer(BukaDaftarBuku) 
                if CekFileDaftarBuku == False: 
                    TulisDaftarBuku.writerow(['JudulBuku', 'Penulis', 'Tahun Terbit', 'Kategori', 'Jumlah Buku']) 
                    
                TulisDaftarBuku.writerow([JudulBuku, Penulis, TahunTerbit, Kategori, JumlahBuku])
            os.system("cls")
            print(f'''#{'='*70}#\n#{"DATA BUKU TELAH TERSIMPAN".center(70)}#\n#{"-"*70}#\n#{"MOHON MASUKKAN DATA KEMBALI".center(70)}#\n#{"="*70}#''')
            input("")
            MenambahkanDataBukuLagi()
        else:
            TampilanMenuAdmin()
#MENAMBAH BUKU

#MENGHAPUS BUKU
def MenghapusDataBuku():
    """Bagian ini akan meminta pengguna untuk memasukkan indeks buku yang ditampilkan, lalu program akan secara otomatis menghapus data tersebut dari file DaftarBuku.csv"""
    os.system("cls") 
    BacaDataBuku = pd.read_csv("DaftarBuku.csv")
    if len(BacaDataBuku) > 0: 
        print(f"""{f"#{'='*70}#".center(78)}\n{f"#{'MENGHAPUS DATA BUKU'.center(70)}#".center(78)}\n{f"#{'-'*70}#".center(78)}\n{f"#{f'SILAHKAN MASUKKAN INDEKS BUKU'.center(70)}#".center(78)}\n{f"#{'='*70}#".center(78)}""")    
        print(tabulate(BacaDataBuku, headers='keys', tablefmt='grid', numalign="center", stralign="center")) 
        BukuHapus = input("Index Buku Manakah yang Ingin Dihapus ? : ")
        if BukuHapus.isdigit() and len(BukuHapus): 
            BukuHapus = int(BukuHapus) + 1 
            with open("DaftarBuku.csv", 'r') as file_csv: 
                BacaDataBuku = list(csv.reader(file_csv)) 
                if 0 < BukuHapus <= len(BacaDataBuku) - 1: 
                    BacaDataBuku.pop(BukuHapus)
                    Keputusan = input("Tekan [Y] Untuk Menghapus Data Buku, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
                    if Keputusan == "Y":
                        with open("DaftarBuku.csv", 'w', newline='') as file_csv: 
                            TulisDataAdmin = csv.writer(file_csv) 
                            TulisDataAdmin.writerows(BacaDataBuku)
                            os.system("cls")
                            print(f"""{f"#{'='*70}#".center(78)}\n{f"#{'BUKU TELAH DI HAPUS'.center(70)}#".center(78)}\n{f"#{'-'*70}#".center(78)}\n{f"#{f'TEKAN ENTER UNTUK LANJUT'.center(70)}#".center(78)}\n{f"#{'='*70}#".center(78)}""")
                            input("")
                        HapusLagi = input("Tekan Y Untuk Menghapus Data Buku Kembali, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper() 
                        if HapusLagi == "Y":
                            MenghapusDataBuku()
                        else:
                            TampilanMenuAdmin()
                    else:
                        TampilanMenuAdmin()
                else:
                    print("Indeks yang dimasukkan melebihi jumlah data yang ada")
                    input("")
                    TampilanMenuAdmin()
        else: 
            print("Masukkan angka sebagai indeks buku")
            input("")
            TampilanMenuAdmin()
    else:
        print(f"""#{'='*70}#\n#{'DATA BUKU TIDAK ADA'.center(70)}#\n#{'='*70}#""")
        input("")
        TampilanMenuAdmin()
#MENGHAPUS BUKU

#MENAMPILKAN DATA BUKU
def MelihatDataBuku():
    """Bagian ini pengguna akan ditampilkan data yang ada didalam file DaftarBuku.csv dalam bentuk tabel"""
    os.system("cls") 
    CekFileDaftarBuku = os.path.isfile("DaftarBuku.csv") 
    BacaDataBuku = pd.read_csv("DaftarBuku.csv") 
    if CekFileDaftarBuku == True and len(BacaDataBuku) > 0: 
        print(f"""{f"#{'='*70}#".center(78)}\n{f"#{'DATA SELURUH BUKU'.center(70)}#".center(78)}\n{f"#{'='*70}#".center(78)}""")
        print(tabulate(BacaDataBuku, headers='keys', tablefmt='grid', numalign="center")) 
        input("Enter untuk kembali")
        TampilanMenuAdmin()
    else:
        print(f"""#{'='*70}#\n#{'DATA BELUM ADA'.center(70)}#\n#{'='*70}#""")
        input("")
        TampilanMenuAdmin()
#MENAMPILKAN DATA BUKU

#MEMASUKKAN DATA BUKU KEMBALI
def MenambahkanDataBukuLagi():
    """Bagian ini pengguna akan diberikan pilihan apakah pengguna akan memasukkan data buku kembali"""
    DataBukuKembali = input("Tekan Y Untuk Menambahkan Data Buku Kembali, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
    if DataBukuKembali == "Y":
        MenambahkanDataBuku()
    else:
        TampilanMenuAdmin()
#MEMASUKKAN DATA BUKU KEMBALI
# ------------------------------------------------------SEMUA TENTANG BUKU------------------------------------------------------- #

# ------------------------------------------------------SEMUA TENTANG ADMIN------------------------------------------------------ #

#MENAMBAHKAN DATA ADMIN
def MenambahkanDataAdmin():
    """Bagian ini akan meminta pengguna untuk memasukkan Nama, Asal, Email, Nomor Telepon, Username dan Password admin yang selanjutnya akan dimasukkan kedalam file DataAdmin.csv"""
    os.system("cls")
    print(f"""#{"="*70}#\n#{"MENAMBAHKAN DATA ADMIN".center(70)}#\n#{"-"*70}#\n#{"MASUKKAN DATA-DATA ADMIN".center(70)}#\n#{"="*70}#""")
    NamaAdmin = input("Nama : ")                
    AsalAdmin = input("Asal : ")                
    EmailAdmin = input("E-mail : ")             
    NomorTelepon = input("Nomor Telepon : ")    
    
    if len(NamaAdmin) < 2 or len(AsalAdmin) < 2 or len(NomorTelepon) < 10  or len(EmailAdmin) < 2 or "@" not in EmailAdmin or NomorTelepon.isdigit() == False:
        os.system("cls")
        print("Mohon Maaf Data Yang Anda Masukkan Kurang Sesuai")
        input("")
        TampilanMenuSuperAdmin()
    else: 
        os.system("cls") 
        print(f"""#{"="*70}#\n#{"MASUKKAN USERNAME DAN PASSWORD ADMIN".center(70)}#\n#{"="*70}#""")
        UsernameAdmin = input("Username : ")        
        PasswordAdmin = input("Password : ")
        if len(UsernameAdmin) > 3 and len(PasswordAdmin) > 3:
            CekFileDataAdmin = os.path.isfile("DataAdmin.csv")
            Keputusan = input("Tekan [Y] Untuk Menyimpan Data Admin, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
            if  Keputusan == "Y":
                if CekFileDataAdmin == False:
                    with open("DataAdmin.csv", "a", newline='') as BukaDataAdmin: 
                        TulisDataAdminBaru = csv.writer(BukaDataAdmin)
                        TulisDataAdminBaru.writerow(['Username', 'Password', 'Nama', 'Asal', 'Email', 'NomorTelepon'])
                        TulisDataAdminBaru.writerow([UsernameAdmin, PasswordAdmin, NamaAdmin, AsalAdmin, EmailAdmin, NomorTelepon]) 
                else:
                    with open("DataAdmin.csv", "a", newline='') as BukaDataAdmin: 
                        TulisDataAdminBaru = csv.writer(BukaDataAdmin) 
                        TulisDataAdminBaru.writerow([UsernameAdmin, PasswordAdmin, NamaAdmin, AsalAdmin, EmailAdmin, NomorTelepon]) 
                        os.system("cls") 
                        print(f"""#{"="*70}#\n#{"DATA TELAH DITAMBAHKAN".center(70)}#\n#{"-"*70}#\n#{"TEKAN ENTER UNTUK KEMBALI".center(70)}#\n#{"="*70}#""")
                        input("")
                DataAdminKembali()
            else:
                TampilanMenuSuperAdmin()
        else:
            print("Mohon Maaf Data Yang Anda Masukkan Kurang Sesuai")
            input("")
            TampilanMenuSuperAdmin()
#MENAMBAHKAN DATA ADMIN

#MENGHAPUS DATA ADMIN
def MenghapusDataAdmin():
    """Bagian ini pengguna akan diminta untuk memasukkan indeks yang telah ditampilkan lalu secara otomatis program akan menghapus data tersebut dari file csv"""
    os.system("cls") 
    
    BacaDataAdmin = pd.read_csv("DataAdmin.csv")
    if len(BacaDataAdmin) > 0:
        print(f"""{f"#{'='*70}#".center(121)}\n{f"#{'MENGHAPUS DATA ADMIN'.center(70)}#".center(121)}\n{f"#{'='*70}#".center(121)}""")
        print(tabulate(BacaDataAdmin, headers='keys', tablefmt='grid')) 
        AdminHapus = input("Index Manakah yang Ingin Dihapus ? : ") 
        if AdminHapus.isdigit() and len(AdminHapus) > 0: 
            AdminHapus = int(AdminHapus) + 1 
            with open("DataAdmin.csv", 'r') as file_csv: 
                BacaDataAdmin = list(csv.reader(file_csv))  
                if 0 < AdminHapus <= len(BacaDataAdmin) - 1: 
                    BacaDataAdmin.pop(AdminHapus)
                    Keputusan = input("Tekan [Y] Untuk Menghapus Data, Tekan Tombol [N] atau Lainnya Untuk Kembali : ").upper()
                    if Keputusan == "Y":
                        with open("DataAdmin.csv", 'w', newline='') as file_csv: 
                            TulisDataAdmin = csv.writer(file_csv) 
                            TulisDataAdmin.writerows(BacaDataAdmin)
                            os.system("cls")
                            print(f"""#{'='*70}#\n#{'DATA TELAH TERHAPUS'.center(70)}#\n#{'='*70}#""")
                        HapusLagi = input("Tekan [Y] Untuk Menghapus Data Lagi, Tekan Tombol [N] atau Lainnya Untuk Kembali : ").upper() 
                        if HapusLagi == "Y":
                            MenghapusDataAdmin()
                        else:
                            TampilanMenuSuperAdmin()
                    else:
                        TampilanMenuSuperAdmin()
                else:
                    print("Indeks yang dimasukkan melebihi jumlah data yang ada")
                    input("")
                    TampilanMenuSuperAdmin()
        else:
            print("Masukkan angka sebagai indeks admin")
            input(" ")
            TampilanMenuSuperAdmin()
    else:
        print(f"""#{'='*70}#\n#{'DATA ADMIN TIDAK ADA'.center(70)}#\n#{'='*70}#""")
        input("")
        TampilanMenuSuperAdmin()
#MENGHAPUS DATA ADMIN

#MENAMPILKAN DATA ADMIN
def MenampilkanDataAdmin():
    """Pada Bagian ini pengguna akan berikan tampilan data yang ada dalam file DataAdmin.csv"""
    os.system("cls")
    CekFileDataAdmin = os.path.isfile("DataAdmin.csv") 
    if CekFileDataAdmin == True: 
        BacaDataAdmin = pd.read_csv("DataAdmin.csv") 
        print(f"""{f"#{'='*70}#".center(121)}\n{f"#{'DATA SELURUH ADMIN'.center(70)}#".center(121)}\n{f"#{'='*70}#".center(121)}""")
        print(tabulate(BacaDataAdmin, headers='keys', tablefmt='grid')) 
        input("Enter untuk kembali")
        TampilanMenuSuperAdmin()
    else:
        print(f"""#{'='*70}#\n#{'DATA BELUM ADA'.center(70)}#\n#{'='*70}#""")
        input("")
        TampilanMenuSuperAdmin()
#MENAMPILKAN DATA ADMIN

#MEMASUKKAN DATA ADMIN KEMBALI
def DataAdminKembali():
    """Bagian ini akan memberikan pilihan apakah super admin akan menambahkan data admin kembali"""
    DataAdminKembali = input("Tekan [Y] Untuk Menyimpan Data Admin Kembali, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper() 
    if DataAdminKembali == "Y":
        MenambahkanDataAdmin()
    else:
        TampilanMenuSuperAdmin()
#MEMASUKKAN DATA ADMIN KEMBALI

# ------------------------------------------------------SEMUA TENTANG ADMIN----------------------------------------------------------- #

# ------------------------------------------------------SEMUA TENTANG PEMINJAMAN------------------------------------------------------ #

#MENAMBAHKAN DATA PEMINJAMAN
def MenambahkanDataPeminjaman():
    """Pada bagian ini pengguna akan diminta untuk memasukkan nama peminjam dan memilih buku yang akan di pinjam, yang selanjutnya program akan secara otomatid menentukan tanggal
    peminjaman dan tanggal pengembalian buku. lalu menyimpan data peminjaman buku ke dalam file DataPeminjaman.csv"""
    os.system("cls")
    print(f"""#{'='*70}#\n#{'MENAMBAHKAN DATA PEMINJAMAN BUKU'.center(70)}#\n#{'='*70}#""")
    NamaPeminjam = input("Masukkan Nama Peminjam Buku : ")

    if len(NamaPeminjam) != 0 and NamaPeminjam.isdigit() == False:
        os.system("cls")
        BacaDataBuku = pd.read_csv("DaftarBuku.csv") 
        
        ValidasInput = True 
        while ValidasInput == True:
            os.system("cls")
            print(tabulate(BacaDataBuku, headers='keys', tablefmt='grid'))
            BukuYangAkanDipinjam = input("Masukkan Indeks Buku yang Akan Dipinjam : ")
            if BukuYangAkanDipinjam.isdigit(): 
                BukuYangAkanDipinjam = int(BukuYangAkanDipinjam)
                if 0 <= BukuYangAkanDipinjam < len(BacaDataBuku): 
                    break 
                else: 
                    print("Indeks yang anda masukkan melebihi data yang ada. Silahkan masukkan indeks yang valid")
                    input("")
                    ValidasInput == True 
            else:
                print("Masukkan indeks buku yang valid")
                input("")
                ValidasInput == True
                
        with open("DaftarBuku.csv", 'r') as file_csv: 
            ListDataBuku = list(csv.reader(file_csv))
            IndexBuku = int(BukuYangAkanDipinjam) + 1
            if int(ListDataBuku[IndexBuku][4]) > 0:
                os.system("cls")
                #Membuat Variabel Yang Akan Digunakan
                NamaPeminjam = NamaPeminjam
                Buku = BacaDataBuku.iloc[BukuYangAkanDipinjam, 0] 
                TanggalPinjam = datetime.today().strftime('%d-%m-%Y') 
                TenggatPinjam = (datetime.today() + timedelta(days=7)).strftime('%d-%m-%Y')
                
                #Menampilkan Variabel Peminjam 
                print(f"""#{'='*70}#\n#{'DATA PEMINJAM'.center(70)}#\n#{'-'*70}#""")
                print(f"""#{f"Nama Peminjam : {NamaPeminjam}".center(70)}#""")
                print(f"""#{f"Judul Buku : {Buku}".center(70)}#""")
                print(f"""#{f"Tanggal Peminjaman : {TanggalPinjam}".center(70)}#""")
                print(f"""#{f"Tenggat Pengembalian : {TenggatPinjam}".center(70)}#""")
                print(f"""#{'='*70}#""")
                
                #Keputusan Admin
                Keputusan = input("Tekan [Y] Untuk Menyimpan Data Peminjaman, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
                if Keputusan == "Y":
                    
                    #Mengurangi Jumlah Buku Dalam File DaftarBuku.csv
                    JumlahDataBukuBaru = int(ListDataBuku[IndexBuku][4]) - 1
                    ListDataBuku[IndexBuku][4] = str(JumlahDataBukuBaru)
                    with open("DaftarBuku.csv", 'w', newline='') as DataBukuBaru: 
                        UpdateDataBukuBaru = csv.writer(DataBukuBaru)
                        UpdateDataBukuBaru.writerows(ListDataBuku)
                    
                    #Menambahkan Data Peminjaman
                    CekFileDataPinjam = os.path.isfile("DataPeminjaman.csv") 
                    if CekFileDataPinjam == False: #Jika file tidak tersedia
                        with open("DataPeminjaman.csv", "a", newline='') as BukaDataPinjam: 
                            TulisDataPinjam = csv.writer(BukaDataPinjam)
                            TulisDataPinjam.writerow(['Nama Peminjam', 'Judul Buku', 'Tanggal Peminjaman', 'Tenggat Pengembalian'])
                            TulisDataPinjam.writerow([NamaPeminjam, Buku, TanggalPinjam, TenggatPinjam]) 
                            os.system("cls") 
                            print(f"""#{'='*70}#\n#{'DATA TELAH DITAMBAHKAN'.center(70)}#\n#{'-'*70}#\n#{'TEKAN ENTER UNTUK LANJUT'.center(70)}#\n#{'='*70}#""")
                            input("")
                    else:
                        with open("DataPeminjaman.csv", "a", newline='') as BukaDataPinjam:
                            TulisDataPinjam = csv.writer(BukaDataPinjam)
                            TulisDataPinjam.writerow([NamaPeminjam, Buku, TanggalPinjam, TenggatPinjam]) 
                            os.system("cls") 
                            print(f"""#{'='*70}#\n#{'DATA TELAH DITAMBAHKAN'.center(70)}#\n#{'-'*70}#\n#{'TEKAN ENTER UNTUK LANJUT'.center(70)}#\n#{'='*70}#""")
                            input("")
                    MasukkanDataPeminjamanKembali()
                else:
                    TampilanMenuAdmin()
            else:
                print("Mohon Maaf, buku yang anda pilih sedang habis")
                input("")
                TampilanMenuAdmin()
    else:
        print("Masukkan Nama Dengan Benar")
        input("")
        TampilanMenuAdmin()
#MENAMBAHKAN DATA PEMINJAMAN

#MENAMPILKAN DATA PEMINJAMAN
def MenampilkanDataPeminjaman():
    """Pada bagian ini pengguna akan disajikan data peminjaman yang ada"""
    os.system("cls")
    CekFileDataPeminjaman = os.path.isfile("DataPeminjaman.csv")
    if CekFileDataPeminjaman == True:
        print(f"""{f"#{'='*70}#".center(90)}\n{f"#{'DATA PEMINJAMAN BUKU'.center(70)}#".center(90)}\n{f"#{'='*70}#".center(90)}""")
        BacaDataPeminjaman = pd.read_csv("DataPeminjaman.csv")
        print(tabulate(BacaDataPeminjaman, headers='keys', tablefmt='grid'))
        input("Enter untuk kembali")
        TampilanMenuAdmin()
    else:
        print(f"""#{'='*70}#\n#{'DATA BELUM ADA'.center(70)}#\n#{'='*70}#""")
        input("")
        TampilanMenuAdmin()

#MENAMPILKAN DATA PEMINJAMAN

#UPDATE TANGGAL PEMINJAMAN
def UpdateTanggalPeminjaman():
    """Pada bagian ini pengguna akan diminta untuk memilih indeks peminjam yang akan diedit, lalu sistem akan secara otomatis mengupdate tanggal peminjaman dan juga tenggat
    pengembalian, lalu data akan kembali disimpan pada file DataPeminjaman.csv""" 
    os.system("cls")
    BacaDataPeminjam = pd.read_csv("DataPeminjaman.csv") 
    if BacaDataPeminjam.empty == False:
        ValidasInput = True 
        while ValidasInput == True:
            os.system("cls")
            print(f"""{f"#{'='*70}#".center(90)}\n{f"#{'UPDATE TANGGAL PEMINJAMAN'.center(70)}#".center(90)}\n{f"#{'='*70}#".center(90)}""")
            print(tabulate(BacaDataPeminjam, headers='keys', tablefmt='grid'))
            IndexPeminjam = input("Masukkan Indeks Peminjam : ")
            if IndexPeminjam.isdigit(): 
                IndexPeminjam=int(IndexPeminjam) 
                if IndexPeminjam < len(BacaDataPeminjam): 
                    break 
                else : 
                    print("Indeks yang anda masukkan melebihi jumlah data")
                    input("")
                    ValidasInput = True 
            else : 
                print("Masukkan angka sebagai indeks peminjam yang akan diedit")
                input("")
                ValidasInput = True 
        KeputusanAdmin = input("Tekan [Y] Untuk Menyimpan Memperbarui Peminjaman, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
        if KeputusanAdmin == "Y":
            with open("DataPeminjaman.csv", "r") as FilePeminjaman: 
                IndexListPeminjam = IndexPeminjam + 1
                ListPeminjaman = list(csv.reader(FilePeminjaman)) 
                TanggalPinjamBaru = datetime.today().strftime('%d-%m-%Y') 
                TenggatPinjamBaru = (datetime.today() + timedelta(days=7)).strftime('%d-%m-%Y') 
                ListPeminjaman[IndexListPeminjam][2] = TanggalPinjamBaru 
                ListPeminjaman[IndexListPeminjam][3] = TenggatPinjamBaru 
            with open("DataPeminjaman.csv", "w", newline='') as UpdatePeminjaman:
                UpdateTanggalPeminjaman = csv.writer(UpdatePeminjaman) 
                UpdateTanggalPeminjaman.writerows(ListPeminjaman)
                os.system("cls")
                print(f"""#{'='*70}#\n#{'DATA TELAH DIUBAH'.center(70)}#\n#{'-'*70}#\n#{'TEKAN ENTER UNTUK LANJUT'.center(70)}#\n#{'='*70}#""")
                input("")
        else:
            TampilanMenuAdmin()
        TampilanMenuAdmin()
    else:
        print("Data Kosong")
        input("Enter Untuk Kembali")
        TampilanMenuAdmin()
#UPDATE TANGGAL PEMINJAMAN

# PENGEMBALIAN BUKU
def PengembalianBuku():
    """Pada bagian ini pengguna akan diminta untuk memasukkan nama peminjam dan memilih indeks peminjaman yang akan dikembalikan, yang selanjutnya program akan menghitung selisih
    hari dari tenggat peminjaman, jika selisih hari kurang dari 0 maka buku dianggap dikembalikan tepat waktu dan data peminjaman akan dimasukkan histori peminjaman,
    namun jika selisih hari lebih dari 0 maka pengembalian buku dianggap terlambat dan data peminjaman akan berpindah kedalam file datadenda.csv"""
    os.system("cls")
    print(f"""#{'='*70}#\n#{'PENGEMBALIAN BUKU'.center(70)}#\n#{'='*70}#""")
    NamaPengembali = input("Masukkan Nama Peminjam : ")
    BacaDataPeminjaman = pd.read_csv("DataPeminjaman.csv") 
    Peminjam = BacaDataPeminjaman[BacaDataPeminjaman['Nama Peminjam'] == NamaPengembali] 
    
    if BacaDataPeminjaman.empty == False and Peminjam.empty == False:
        ValidasInputPengembalian = True 
        while ValidasInputPengembalian == True: 
            os.system("cls")
            print(tabulate(Peminjam, headers='keys', tablefmt='grid'))
            IndexPeminjam = input("Masukkan Indeks Peminjam : ") 
            if IndexPeminjam.isdigit(): 
                IndexPeminjam = int(IndexPeminjam) 
                if 0 <= IndexPeminjam < len(BacaDataPeminjaman): 
                    break 
                else: 
                    print("Indeks yang dimasukkan melebihi jumlah data. Masukkan indeks yang valid.")
                    input("")
                    ValidasInputPengembalian == True 
            else: 
                print("Masukkan angka sebagai indeks peminjam.")
                input("")
                ValidasInputPengembalian == True 
        
        Pengembalian = datetime.today() 
        SelisihHari = (Pengembalian - pd.to_datetime(BacaDataPeminjaman.iloc[IndexPeminjam, 3], format ="%d-%m-%Y")).days 
        NamaPeminjamKembali = BacaDataPeminjaman.iloc[IndexPeminjam, 0] 
        JudulBukuKembali = BacaDataPeminjaman.iloc[IndexPeminjam, 1] 
        TanggalPeminjamanKembali = BacaDataPeminjaman.iloc[IndexPeminjam, 2] 
        TenggatPengembalianKembali = BacaDataPeminjaman.iloc[IndexPeminjam, 3] 
    
        if SelisihHari <= 0: 
            StatusPengembalian = "Tepat Waktu" 
            JumlahDenda = "Tidak Ada"
            StatusDenda = "Tidak Ada"
        
            CekFileHistoryPertama = os.path.isfile("HistoryPeminjaman.csv") 
    
            if CekFileHistoryPertama == False: 
                with open("HistoryPeminjaman.csv", "a", newline='') as BukaHistory:
                    TulisHistoryPertama = csv.writer(BukaHistory) 
                    TulisHistoryPertama.writerow(['Nama Peminjam', 'Judul Buku', 'Tanggal Peminjaman', 'Tenggat Pengembalian', 'Status Pengembalian', 'Jumlah Denda', 'Status Denda']) 
                    TulisHistoryPertama.writerow([NamaPeminjamKembali, JudulBukuKembali, TanggalPeminjamanKembali, TenggatPengembalianKembali, StatusPengembalian, JumlahDenda, StatusDenda]) 
            else:
                with open("HistoryPeminjaman.csv", "a", newline='') as BukaHistory:
                    TulisHistoryPertama = csv.writer(BukaHistory) 
                    TulisHistoryPertama.writerow([NamaPeminjamKembali, JudulBukuKembali, TanggalPeminjamanKembali, TenggatPengembalianKembali, StatusPengembalian, JumlahDenda, StatusDenda])
                    
            with open("DataPeminjaman.csv", 'r') as BukaPeminjaman: 
                BacaDataPeminjaman1 = list(csv.reader(BukaPeminjaman)) 
                BacaDataPeminjaman1.pop(IndexPeminjam + 1) 
            with open("DataPeminjaman.csv", 'w', newline='') as BukaPeminjaman: 
                TulisDataPeminjaman = csv.writer(BukaPeminjaman) 
                TulisDataPeminjaman.writerows(BacaDataPeminjaman1)
            os.system("cls")
            print(f"""#{'='*70}#\n#{'BUKU DIKEMBALIKAN TEPAT WAKTU'.center(70)}#\n#{'='*70}#""")
            input("")
            
        elif SelisihHari > 0: 
            StatusPengembalian = "Terlambat"
            JumlahDenda = 500 * SelisihHari
            StatusDenda = "Belum Dibayar"
            
            os.system("cls")
            print(f"""#{'='*70}#\n#{'BUKU DIKEMBALIKAN TERLAMBAT'.center(70)}#\n#{'='*70}#\n#{'KETERANGAN DENDA'.center(70)}#\n#{'='*70}#""")
            print(f"""#{f"Nama Peminjam : {NamaPeminjamKembali}".center(70)}#""")
            print(f"""#{f"Judul Buku : {JudulBukuKembali}".center(70)}#""")
            print(f"""#{f"Lama Keterlambatan : {SelisihHari} Hari".center(70)}#""")
            print(f"""#{f"Jumlah Denda : Rp.{JumlahDenda}".center(70)}#""")
            print(f"""#{'='*70}#""")
            print(f"""#{'='*70}#\n#{'TEKAN ENTER UNTUK LANJUT'.center(70)}#\n#{'='*70}#""")
            input("")
            
            CekFileDataDendaPertama = os.path.isfile("DataDenda.csv") 
            if CekFileDataDendaPertama == False: 
                with open("DataDenda.csv", "a", newline='') as BukaDataDenda: 
                    TulisDenda = csv.writer(BukaDataDenda) 
                    TulisDenda.writerow(['Nama Peminjam', 'Judul Buku', 'Tanggal Peminjaman', 'Tenggat Pengembalian', 'Status Pengembalian', 'Jumlah Denda', 'Status Denda'])  
                    TulisDenda.writerow([NamaPeminjamKembali, JudulBukuKembali, TanggalPeminjamanKembali, TenggatPengembalianKembali, StatusPengembalian, JumlahDenda, StatusDenda])
            else:
                with open("DataDenda.csv", "a", newline='') as BukaDataDenda: 
                    TulisDenda = csv.writer(BukaDataDenda)
                    TulisDenda.writerow([NamaPeminjamKembali, JudulBukuKembali, TanggalPeminjamanKembali, TenggatPengembalianKembali, StatusPengembalian, JumlahDenda, StatusDenda])
                    
            with open("DataPeminjaman.csv", 'r') as BukaPeminjaman: 
                BacaDataPeminjaman = list(csv.reader(BukaPeminjaman)) 
                BacaDataPeminjaman.pop(IndexPeminjam + 1) 
            with open("DataPeminjaman.csv", 'w', newline='') as BukaPeminjaman: 
                TulisDataPeminjaman = csv.writer(BukaPeminjaman) 
                TulisDataPeminjaman.writerows(BacaDataPeminjaman) 
                    
        with open("DaftarBuku.csv", 'r') as file_csv: 
            ListDataBuku = list(csv.reader(file_csv))
            for row in ListDataBuku:
                if row[0] == JudulBukuKembali:
                    row[4] = str(int(row[4]) + 1)
                    with open("DaftarBuku.csv", 'w', newline='') as DataBukuBaru: 
                        UpdateDataBukuBaru = csv.writer(DataBukuBaru)
                        UpdateDataBukuBaru.writerows(ListDataBuku)
                else:
                    pass
    elif Peminjam.empty == True:
        print(f"""#{"="*70}#\n#{"DATA PEMINJAMAN TIDAK ADA".center(70)}#\n#{"-"*70}#\n#{"TEKAN ENTER UNTUK KEMBALI".center(70)}#\n#{"="*70}#""")
        input("")
        TampilanMenuAdmin()
    TampilanMenuAdmin()
# PENGEMBALIAN BUKU SELESAI

# MELIHAT DATA DENDA
def MelihatDataDenda():
    """Pada bagian ini pengguna akan disajikan data denda yang ada"""
    os.system("cls")
    CekFileDataDenda = os.path.isfile("DataDenda.csv")
    if CekFileDataDenda == True:
        BacaDataDenda = pd.read_csv("DataDenda.csv")
        print(tabulate(BacaDataDenda, headers='keys', tablefmt='grid'))
        input("Enter Untuk Kembali")
        TampilanMenuAdmin()
    else:
        print(f"""#{"="*70}#\n#{"DATA TIDAK ADA ATAU DATA KOSONG".center(70)}#\n#{"-"*70}#\n#{"TEKAN ENTER UNTUK KEMBALI".center(70)}#\n#{"="*70}#""")
        input("")
        TampilanMenuAdmin()
# MELIHAT DATA DENDA

# PEMBAYARAN DENDA
def PembayaranDenda():
    """Pada bagian ini pengguna akan diminta untuk memasukkan nama pengembali yang memiliki denda dan diminta untuk memilih indeks denda yang akan dibayar, apabila 
    peminjam membayarkan dendanya maka data denda akan di rubah dan dipindah kedalam file HistoryPeminjaman.csv"""
    os.system("cls")
    print(f"""#{'='*70}#\n#{'PEMBAYARAN DENDA'.center(70)}#\n#{'='*70}#""")
    NamaPengembali = input("Masukkan Nama Peminjam : ")
    BacaDataDenda = pd.read_csv("DataDenda.csv") 
    Peminjam = BacaDataDenda[BacaDataDenda['Nama Peminjam'] == NamaPengembali]
    if len(NamaPengembali) > 0:
        if len(Peminjam) > 0:
            if BacaDataDenda.empty == False and Peminjam.empty == False:
                ValidasInput = True 
                while ValidasInput == True: 
                    os.system("cls")
                    print(tabulate(Peminjam, headers='keys', tablefmt='grid'))
                    IndexDenda = input("Masukkan Indeks Peminjam : ")
                    if IndexDenda.isdigit(): 
                        IndexDenda=int(IndexDenda) 
                        if IndexDenda < len(Peminjam): 
                            break 
                        else :
                            print("Indeks yang anda masukkan melebihi jumlah data")
                            input("")
                            ValidasInput = True
                    else :
                        print("Masukkan angka sebagai indeks denda yang akan dibayarkan")
                        input("")
                        ValidasInput = True
                        
                BayarDenda = input("Apakah denda akan dibayar ? (Y/N) : ").upper()
                if BayarDenda == 'Y': 
                    StatusDenda = "Sudah Dibayar"
                    NamaPembayar = BacaDataDenda.iloc[IndexDenda,0] 
                    Judul = BacaDataDenda.iloc[IndexDenda,1] 
                    TanggalPeminjaman = BacaDataDenda.iloc[IndexDenda,2]
                    TenggatPeminjaman = BacaDataDenda.iloc[IndexDenda,3] 
                    StatusPengembalian = BacaDataDenda.iloc[IndexDenda,4] 
                    JumlahDenda = BacaDataDenda.iloc[IndexDenda,5] 
                    BacaDataDenda.iloc[IndexDenda,6] = StatusDenda 
                    with open("HistoryPeminjaman.csv", "a", newline='') as BukaHistory: 
                        TulisHistori = csv.writer(BukaHistory) 
                        TulisHistori.writerow([NamaPembayar,Judul,TanggalPeminjaman,TenggatPeminjaman,StatusPengembalian,JumlahDenda,BacaDataDenda.iloc[IndexDenda,6]]) 
                    with open("DataDenda.csv", 'r') as BukaDenda: 
                        BacaDenda = list(csv.reader(BukaDenda)) 
                        BacaDenda.pop(IndexDenda + 1) 
                    with open("DataDenda.csv", 'w', newline='') as BukaDenda: 
                        TulisDenda = csv.writer(BukaDenda) 
                        TulisDenda.writerows(BacaDenda)
                    os.system("cls")
                    print(f"""#{"="*70}#\n#{"DENDA TELAH DIBAYAR".center(70)}#\n#{"-"*70}#\n#{"TEKAN ENTER UNTUK KEMBALI".center(70)}#\n#{"="*70}#""")
                    input("")
                    TampilanMenuAdmin()
                else :
                    TampilanMenuAdmin()
            else:
                print(f"""#{"="*70}#\n#{"DATA TIDAK ADA ATAU DATA KOSONG".center(70)}#\n#{"-"*70}#\n#{"TEKAN ENTER UNTUK KEMBALI".center(70)}#\n#{"="*70}#""")
                input("")
                TampilanMenuAdmin()
        else:
            print("Nama Tidak Ditemukan")
            input("")
            TampilanMenuAdmin()
    else:
        print("Nama Tidak Boleh Kosong")
        input("")
        TampilanMenuAdmin()
#PEMBAYARAN DENDA

#MENAMPILKAN HISTORI PEMINJAMAN      
def HistoryPeminjaman():
    """Pada bagian ini pengguna akan disajikan histori dari peminjaman yang telah dilakukan"""
    os.system("cls")
    CekFileDataPeminjaman = os.path.isfile("HistoryPeminjaman.csv")
    if CekFileDataPeminjaman == True:
        print(f"""#{'='*70}#\n#{'HISTORI PEMINJAMAN'.center(70)}#\n#{'='*70}#""")
        BacaHistory = pd.read_csv("HistoryPeminjaman.csv")
        print(tabulate(BacaHistory, headers='keys', tablefmt='grid'))
        input("Enter untuk kembali")
        TampilanMenuAdmin()
    else:
        print(f"""#{"="*70}#\n#{"DATA TIDAK ADA ATAU DATA KOSONG".center(70)}#\n#{"-"*70}#\n#{"TEKAN ENTER UNTUK KEMBALI".center(70)}#\n#{"="*70}#""")
        input("")
        TampilanMenuAdmin()
#MENAMPILKAN HISTORI PEMINJAMAN      

#MEMASUKKAN DATA PEMINJAMAN KEMBALI
def MasukkanDataPeminjamanKembali():
    DataPeminjamanKembali = input("Tekan [Y] Untuk Menyimpan Data Peminjaman, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
    
    if DataPeminjamanKembali == "Y":
        MenambahkanDataPeminjaman()
    else:
        TampilanMenuAdmin()
#MEMASUKKAN DATA PEMINJAMAN KEMBALI

# ------------------------------------------------------SEMUA TENTANG PEMINJAMAN------------------------------------------------------ #

#TAMPILAN MENU SUPER ADMIN 
def TampilanMenuSuperAdmin():
    """Tampilan Menu Super Admin"""
    os.system("cls")
    print("#===================================================================#")
    print("#                      TAMPILAN SUPER MENU ADMIN                    #")
    print("#-------------------------------------------------------------------#")
    print("#                      1. Menambahkan Data Admin                    #")
    print("#                      2. Melihat Data Admin                        #")
    print("#                      3. Menghapus Data Admin                      #")
    print("#                      4. Exit                                      #")
    print("#-------------------------------------------------------------------#")
    print("#               Silahkan Pilih Menu Yang Akan Dijalankan            #")
    print("#===================================================================#")
    PilihanSuperAdmin = input("Pilih Menu yang Ingin Anda Jalankan : ")
    
    if PilihanSuperAdmin == "1":
        MenambahkanDataAdmin()
    elif PilihanSuperAdmin == "2":
        MenampilkanDataAdmin()
    elif PilihanSuperAdmin == "3":
        MenghapusDataAdmin()
    elif PilihanSuperAdmin == "4":
        ExitSuperAdmin()
    else:
        input("Input yang Anda Masukkan Salah, Masukkan Kembali")
        TampilanMenuSuperAdmin()
#TAMPILAN MENU SUPER ADMIN 

def ExitSuperAdmin():
    """Bagian ini akan mengeluarkan super admin dari aplikasi"""
    PilihanExitSuperAdmin = input("Tekan [Y] Untuk Keluar, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
    if PilihanExitSuperAdmin == "Y":
        TampilanAkhir()
    else:
        TampilanMenuSuperAdmin()

#TAMPILAN MENU ADMIN
def TampilanMenuAdmin():
    """Tampilan Menu Admin"""
    os.system("cls")
    print("#===================================================================#")
    print("#                          TAMPILAN MENU ADMIN                      #")
    print("#----------------------------------+++------------------------------#")
    print("# 1. Menambah Data Buku             | 6. Update Tanggal Peminjaman  #")
    print("#----------------------------------+++------------------------------#")
    print("# 2. Menghapus Data Buku            | 7. Pengembalian Buku          #")
    print("#----------------------------------+++------------------------------#")
    print("# 3. Melihat Data Buku              | 8. Melihat Data Denda         #")
    print("#----------------------------------+++------------------------------#")
    print("# 4. Menambah Data Peminjaman Buku  | 9. Pembayaran Denda           #")
    print("#----------------------------------+++------------------------------#")
    print("# 5. Melihat Data Peminjaman Buku   | 10. Histori Peminjaman Buku   #")
    print("#----------------------------------+++------------------------------#")
    print("#                               11. Exit                            #")
    print("#-------------------------------------------------------------------#")
    print("#               Silahkan Pilih Menu Yang Akan Dijalankan            #")
    print("#===================================================================#")
    
    PilihanAdmin = input("Pilih Menu yang Ingin Anda Jalankan : ")

    if PilihanAdmin == "1":
        MenambahkanDataBuku()
    elif PilihanAdmin == "2":
        MenghapusDataBuku()
    elif PilihanAdmin == "3":
        MelihatDataBuku()
    elif PilihanAdmin == "4":
        MenambahkanDataPeminjaman()
    elif PilihanAdmin == "5":
        MenampilkanDataPeminjaman()
    elif PilihanAdmin == "6":
        UpdateTanggalPeminjaman()
    elif PilihanAdmin == "7":
        PengembalianBuku()
    elif PilihanAdmin == "8":
        MelihatDataDenda()
    elif PilihanAdmin == "9":
        PembayaranDenda()
    elif PilihanAdmin == "10":
        HistoryPeminjaman()
    elif PilihanAdmin == "11":
        ExitAdmin()
    else:
        input("Input yang Anda Masukkan Salah, Masukkan Kembali")
        TampilanMenuAdmin()
#TAMPILAN MENU ADMIN

#ADMIN KELUAR
def ExitAdmin():
    """Bagian ini akan mengeluarkan admin dari aplikasi"""
    PilihanExitAdmin = input("Tekan [Y] Untuk Keluar, Tekan Tombol [N] atau Lainnya Untuk Kembali ke Menu :").upper()
    if PilihanExitAdmin == "Y":
        TampilanAkhir()
    else:
        TampilanMenuAdmin()
#ADMIN KELUAR

def TampilanAkhir():
    os.system("cls")
    print(f"""#{'='*70}#\n#{'TERIMA KASIH'.center(70)}#\n#{'='*70}#""")
    return

LaunchPage()