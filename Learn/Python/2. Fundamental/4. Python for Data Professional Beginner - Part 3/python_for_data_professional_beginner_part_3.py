# -*- coding: utf-8 -*-
"""Python for Data Professional Beginner - Part 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/112tv90m2_oCuga1yrAEWK0sECqP0wWFy

# Class dan Objek dalam Python - Part 1
"""

class Karyawan:
    pass

aksara = Karyawan()
senja = Karyawan()

"""# Class dan Objek dalam Python - Part 3"""

class Karyawan:
    nama_perusahaan = 'ABC'
aksara = Karyawan()
senja = Karyawan()

# Akses class attribute
print(aksara.__class__.nama_perusahaan)

print(senja.__class__.nama_perusahaan)

class Karyawan:
    nama_perusahaan = 'ABC'
aksara = Karyawan()
senja = Karyawan()
aksara.__class__.nama_perusahaan = 'DEF'
print(aksara.__class__.nama_perusahaan)

# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'

# Inisiasi object yang dinyatakan dalam variabel aksara dan senja
aksara = Karyawan()
senja = Karyawan()

# Cetak nama perusahaan melalui penggunaan keyword __class__
# pada class attribute nama_perusahaan
print(aksara.__class__.nama_perusahaan)

# Ubah nama_perusahaan menjadi 'DEF'
aksara.__class__.nama_perusahaan = 'DEF'

# Cetak nama_perusahaan objek aksara dan senja
print(aksara.__class__.nama_perusahaan)
print(senja.__class__.nama_perusahaan)

"""# Class dan Objek dalam Python - Part 4"""

class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)
print(aksara.nama + ', Usia ' + str(aksara.usia) + ', Pendapatan ' + str(aksara.pendapatan))

print(senja.nama + ', Usia ' + str(senja.usia) + ', Pendapatan ' + str(senja.pendapatan))

# Quiz
class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        if usia > 30:
            self.pendapatan += 1500000

karyawan_1 = Karyawan('Budi', 35, 7500000)
karyawan_2 = Karyawan('Didi', 30, 8000000)

total_pengeluaran = karyawan_1.pendapatan + karyawan_2.pendapatan
print(total_pengeluaran)

# Quiz
class Karyawan:
    nama_perusahaan = 'ABC'
    tunjangan_transportasi = 500000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan

karyawan_1 = Karyawan('Budi', 35, 5000000)
karyawan_2 = Karyawan('Didi', 30, 5000000)
karyawan_1.__class__.nama_perusahaan = 1000000

total_pengeluaran = karyawan_1.__class__.tunjangan_transportasi
total_pengeluaran += karyawan_2.__class__.tunjangan_transportasi
total_pengeluaran += karyawan_1.pendapatan
total_pengeluaran += karyawan_2.pendapatan

print(total_pengeluaran)

"""# Behavior pada Class"""

class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
    	self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
    	return self.pendapatan + self.pendapatan_tambahan

aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)

aksara.lembur()

senja.tambahan_proyek(2500000)

print('Pendapatan Total Aksara: ' + str(aksara.total_pendapatan()))
print('Pendapatan Total Senja: ' + str(senja.total_pendapatan()))

"""# Tugas Praktek"""

# Definisikan class Karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# Definisikan class Perusahaan
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon): 
        self.nama = nama
        self.alamat = alamat 
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan 
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)

# Definisikan perusahaan
perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman, Blok 11', '(021) 95205XX')
# Definisikan nama-nama karyawan
karyawan_1 = Karyawan('Ani', 25, 8500000, 100000)
karyawan_2 = Karyawan('Budi', 28, 12000000, 150000)
karyawan_3 = Karyawan('Cici', 30, 15000000, 200000)
# Aktifkan karyawan di perusahaan ABC
perusahaan.aktifkan_karyawan(karyawan_1) 
perusahaan.aktifkan_karyawan(karyawan_2) 
perusahaan.aktifkan_karyawan(karyawan_3)

"""# Encapsulation pada Python - Part 2"""

class Karyawan:
    nama_perusahaan = 'ABC'
    __insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.__nama = nama
        self.__usia = usia
        self.__pendapatan = pendapatan
        self.__pendapatan_tambahan = 0
    def lembur(self):
        self.__pendapatan_tambahan += self.__insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.__pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.__pendapatan + self.__pendapatan_tambahan
aksara = Karyawan('Aksara', 25, 8500000)

print(aksara.__class__.nama_perusahaan)

print(aksara.__nama) # akan menghasilkan error, karena bersifat private

"""# Inheritance pada Python – Part 1"""

class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

class IlmuwanData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())

senja = IlmuwanData('Senja', 28, 13000000)
senja.tambahan_proyek(2000000)
print(senja.total_pendapatan())

"""# Inheritance pada Python – Part 2"""

class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

class IlmuwanData(Karyawan):
    # Mengubah atribut insentif_lembur yang digunakan pada fungsi lembur()
    insentif_lembur = 500000
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())

# Buat objek karyawan yang bekerja sebagai IlmuwanData
senja = IlmuwanData('Senja', 28, 13000000)
senja.lembur()
print(senja.total_pendapatan())

"""# Polymorphism pada Python - Part 1"""

class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)
    def lembur(self):
        self.pendapatan_tambahan += int(self.pendapatan * 0.1)

aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())

"""# Polymorphism pada Python - Part 2"""

class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)
    def lembur(self):
        super().lembur()
        self.pendapatan_tambahan += int(self.pendapatan * 0.05)

aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())

"""# Tugas Praktek"""

# Definisikan class Karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# Definisikan class TenagaLepas sebagai child class dari
# class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += nilai_proyek  * 0.01

# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# Definisikan class TenagaLepas sebagai child class dari
# class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.01

# Definisikan class AnalisData sebagai child class dari
# class Karyawan
class AnalisData(Karyawan):
	pass

# Definisikan class IlmuwanData sebagai child class dari
# class Karyawan
class IlmuwanData(Karyawan):
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += 0.1 * nilai_proyek

# Definisikan class PembersihData sebagai child class dari
# class TenagaLepas
class PembersihData(TenagaLepas):
	pass

# Definisikan class DokumenterTeknis sebagai child class dari
# class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def tambahan_proyek(self, jumlah_tambahan): 
        return

"""# Tugas Praktek"""

class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    ''' 
    usia akan di-set nilainya menjadi 21 saat tidak
    dispesifikasikan dan pendapatan akan di-set nilainya
    menjadi 5000000 saat tidak dispesifikasikan
    '''
    def __init__(self, nama, usia=21, pendapatan=5000000): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# Karyawan baru pertama yang bernama Budi
karyawan_baru1 = Karyawan('Budi')
print(karyawan_baru1.nama)
print(karyawan_baru1.usia)
print(karyawan_baru1.total_pendapatan())

# Karyawan baru ke-2 yang bernama Didi, umur 25
karyawan_baru2 = Karyawan('Didi', 25)
print(karyawan_baru2.nama)
print(karyawan_baru2.usia)
print(karyawan_baru2.total_pendapatan())

# Karyawan baru ke-3 yang bernama Hadi, pendapatan 8000000
karyawan_baru3 = Karyawan('Hadi', pendapatan=8000000)
print(karyawan_baru3.nama)
print(karyawan_baru3.usia)
print(karyawan_baru3.total_pendapatan())

"""# Studi Kasus dari Senja"""

# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan 

# Definisikan class TenagaLepas sebagai child class dari class Karyawan 
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += nilai_proyek  * 0.01

# Definisikan class AnalisData sebagai child class dari class Karyawan 
class AnalisData(Karyawan):
    def __init__(self, nama, usia = 21, pendapatan = 6500000,
				 insentif_lembur = 100000):
        super().__init__(nama, usia, pendapatan, insentif_lembur)

# Definisikan class IlmuwanData sebagai child class dari class Karyawan
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia = 25, pendapatan = 12000000,
				 insentif_lembur = 150000):
        super().__init__(nama, usia, pendapatan,insentif_lembur)
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += 0.1 * nilai_proyek

# Definisikan class PembersihData sebagai child class dari class TenagaLepas
class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 4000000):
        super().__init__(nama, usia, pendapatan)

# Definisikan class DokumenterTeknis sebagai child class dari class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 2500000):
        super().__init__(nama, usia, pendapatan)
        def tambahan_proyek(self, jumlah_tambahan):
            return

# Definisikan class Perusahaan 
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan 
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)
    def total_pengeluaran(self): 
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan() 
        return pengeluaran
    def cari_karyawan(self, nama_karyawan): 
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                return karyawan
        return None

# Create object karyawan sesuai dengan tugasnya masing-masing
# seperti yang dinyatakan dalam tabel.
ani = PembersihData('Ani', 25)
budi = DokumenterTeknis('Budi', 18)
cici = IlmuwanData('Cici')
didi = IlmuwanData('Didi', 32, 20000000)
efi = AnalisData('Efi')
febi = AnalisData('Febi', 28, 12000000)

# Create object perusahaan
perusahaan = Perusahaan('ABC','Jl. Jendral Sudirman, Blok 11', '(021) 95812XX')

# Aktifkan setiap karyawan yang telah didefinisikan
perusahaan.aktifkan_karyawan(ani)
perusahaan.aktifkan_karyawan(budi)
perusahaan.aktifkan_karyawan(cici)
perusahaan.aktifkan_karyawan(didi)
perusahaan.aktifkan_karyawan(efi)
perusahaan.aktifkan_karyawan(febi)

# Cetak keseluruhan total pengeluaran perusahaan
print(perusahaan.total_pengeluaran())