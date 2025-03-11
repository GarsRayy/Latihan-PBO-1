class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis Kendaraan: {self.jenis}, Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")
    
    def bergerak(self):
        print("Kendaraan sedang bergerak...")

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        print(f"Merk: {self.merk}, Jumlah Pintu: {self.jumlah_pintu}")
    
    def bunyikan_klakson(self):
        print("Beep beep! Mobil membunyikan klakson.")

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda  # Private attribute
        self.__harga = harga  # Private attribute
    
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        if value > 0:
            self.__tenaga_kuda = value
        else:
            print("Tenaga kuda harus lebih dari 0!")
    
    def get_harga(self):
        return self.__harga
    
    def set_harga(self, value):
        if value > 0:
            self.__harga = value
        else:
            print("Harga harus lebih dari 0!")
    
    def info_mobil_sport(self):
        print(f"Mobil Sport: {self.merk}, Tenaga Kuda: {self.__tenaga_kuda} HP, Harga: Rp{self.__harga} juta")
    
    def mode_balap(self):
        print("Mobil sport masuk ke mode balap!")

# Contoh penggunaan
mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 700, 15000)
mobil_sport.info_kendaraan()
mobil_sport.info_mobil()
mobil_sport.info_mobil_sport()
mobil_sport.bunyikan_klakson()
mobil_sport.mode_balap()

# Menggunakan getter dan setter
print("Tenaga Kuda Sebelum: ", mobil_sport.get_tenaga_kuda())
mobil_sport.set_tenaga_kuda(750)
print("Tenaga Kuda Sesudah: ", mobil_sport.get_tenaga_kuda())
