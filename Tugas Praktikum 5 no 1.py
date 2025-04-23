import random

class Game:
    def __init__(self):
        self.ukuran = 3
        self.papan = [['?' for _ in range(self.ukuran)] for _ in range(self.ukuran)]
        self.__bom_x = random.randint(0, self.ukuran - 1)
        self.__bom_y = random.randint(0, self.ukuran - 1)
        self.kotak_terbuka = 0
        self.total_kotak = self.ukuran ** 2 - 1

    def tampilkan_papan(self):
        print("   " + " ".join(str(i) for i in range(self.ukuran)))
        print("  " + "-" * (2 * self.ukuran + 1))
        for i, baris in enumerate(self.papan):
            print(f"{i} | " + ' '.join(baris))

    def buka_kotak(self, x, y):
        if not (0 <= x < self.ukuran and 0 <= y < self.ukuran):
            print(" silahkan masukkan 0 - 2 jangan lebih")
            return False

        if self.papan[x][y] != '?':
            print("Kotak ini sudah dibuka, pilih yang lain")
            return False

        if x == self.__bom_x and y == self.__bom_y:
            self.papan[x][y] = 'X'
            self.tampilkan_papan()
            print("Bom ditemukan Kamu kalah")
            return True

        self.papan[x][y] = 'O'
        self.kotak_terbuka += 1

        if self.kotak_terbuka == self.total_kotak:
            self.tampilkan_papan()
            print("Selamat Kamu menang!")
            return True

        return False

    def mainkan(self):
        while True:
            self.tampilkan_papan()
            try:
                x = int(input("Masukkan baris (0-2): "))
                y = int(input("Masukkan kolom (0-2): "))
            except ValueError:
                print("Masukkan angka yang valid!")
                continue

            selesai = self.buka_kotak(x, y)
            if selesai:
                break

if __name__ == "__main__":
    game = Game()
    game.mainkan()
