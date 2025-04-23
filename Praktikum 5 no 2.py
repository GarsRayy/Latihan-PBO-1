import random

WORDS = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

STAGES = [
    """
    ------
    |    |
    |
    |
    |
    |
    |
------------""", """
    ------
    |    |
    |    O
    |
    |
    |
    |
------------""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |
    |
------------""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   /
    |
------------""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   / \\
    |
------------""", """
    ------
    |    |
    |    O
    |  --|
    |    |
    |   / \\
    |
------------""", """
    ------
    |    |
    |    O
    |  --|--
    |    |
    |   / \\
    |
------------"""
]

class HangmanBase:
    def __init__(self):
        self.kata = random.choice(WORDS).upper()
        self.kata_tertebak = ["_" for _ in self.kata]
        self.percobaan = len(STAGES) - 1
        self.huruf_ditebak = set()
        self.__tebakan = ""

    def tampilkan_hangman(self, tries):
        print(STAGES[tries])

    def set_tebakan(self, nilai):
        self.__tebakan = nilai.upper()

    def get_tebakan(self):
        return self.__tebakan

class HangmanGame(HangmanBase):
    def tampilkan_hangman(self, tries):
        super().tampilkan_hangman(tries)

    def mainkan(self):
        while self.percobaan > 0:
            self.tampilkan_hangman(len(STAGES) - 1 - self.percobaan)
            print("Kata: ", " ".join(self.kata_tertebak))
            print("Huruf yang sudah ditebak:", ", ".join(sorted(self.huruf_ditebak)))

            tebakan = input("Tebak huruf atau seluruh kata, hanya yang terdaftar ya: ").strip()
            self.set_tebakan(tebakan)

            current_guess = self.get_tebakan()

            if len(current_guess) == len(self.kata) and current_guess.isalpha():
                if current_guess == self.kata:
                    print("🎉 Selamat! Anda menebak kata:", self.kata)
                    break
                else:
                    self.percobaan -= 1
                    print("Kata salah Sisa percobaan:", self.percobaan)
                    continue

            elif len(current_guess) != 1 or not current_guess.isalpha():
                print("Masukkan satu huruf atau seluruh kata yang valid sesuaikan jumlah '---' nya ")
                continue

            if current_guess in self.huruf_ditebak:
                print("Anda sudah menebak huruf ini.")
                continue

            self.huruf_ditebak.add(current_guess)

            if current_guess in self.kata:
                for i, huruf in enumerate(self.kata):
                    if huruf == current_guess:
                        self.kata_tertebak[i] = current_guess
                if "_" not in self.kata_tertebak:
                    print("Selamat! Anda menebak kata:", self.kata)
                    break
            else:
                self.percobaan -= 1
                print("Huruf tidak ditemukan. Sisa percobaan:", self.percobaan)

        if self.percobaan == 0:
            self.tampilkan_hangman(len(STAGES) - 1)
            print("Game over! Kata yang benar adalah:", self.kata)

if __name__ == "__main__":
    game = HangmanGame()
    game.mainkan()
