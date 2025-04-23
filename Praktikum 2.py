from abc import ABC, abstractmethod

# Kelas abstrak sebagai base class
class Hewan(ABC):
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur
    
    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value):
        if isinstance(value, str):
            self._nama = value
        else:
            raise ValueError("Nama harus string!")
    
    @property
    def umur(self):
        return self._umur
    
    @abstractmethod
    def bersuara(self):
        pass
    
    def bergerak(self):
        return "Hewan ini bergerak"

class Kucing(Hewan):
    def __init__(self, nama, umur, berat):
        super().__init__(nama, umur)
        self.berat = berat
    
    def bersuara(self):
        return f"{self.nama} berkata: Meow!"
    
    def __add__(self, other):
        if isinstance(other, Kucing):
            return self.berat + other.berat
        return self.berat + other
    
    def bergerak(self):
        return f"{self.nama} berlari dengan kaki kecilnya"

class Burung(Hewan):
    def __init__(self, nama, umur, lebar_sayap):
        super().__init__(nama, umur)
        self.lebar_sayap = lebar_sayap
    
    def bersuara(self):
        return f"{self.nama} berkata: Cuit cuit!"
    
    def bergerak(self):
        return f"{self.nama} terbang dengan sayap {self.lebar_sayap} cm"

class Robot:
    def bergerak(self):
        return "Robot bergerak dengan roda"

def gerakan_semua(obj):
    return obj.bergerak()

# Main program
def main():
    # Membuat objek
    kucing = Kucing("Mimi", 2, 4.5)
    burung = Burung("Pipit", 1, 20)
    robot = Robot()
    
    print(f"Nama kucing: {kucing.nama}")
    kucing.nama = "Kiko"
    print(f"Nama kucing setelah diubah: {kucing.nama}")
    print(f"Umur kucing: {kucing.umur}")
    
    print("\nPolimorfisme - Override:")
    print(kucing.bersuara())
    print(burung.bersuara())
    
    print("\nOperator Overloading:")
    kucing_lain = Kucing("Wowo", 3, 5.0)
    total_berat = kucing + kucing_lain
    print(f"Total berat dua kucing: {total_berat} kg")
    berat_tambah = kucing + 2.5
    print(f"Berat kucing + 2.5: {berat_tambah} kg")
    print("\nDuck Typing:")
    hewan_list = [kucing, burung, robot]
    for hewan in hewan_list:
        print(gerakan_semua(hewan))

if __name__ == "__main__":
    main()