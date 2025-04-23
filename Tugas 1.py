# Garis Rayya Rabbani 123140018
# Latihan 1

def piramid(tinggi):
    for i in range(1, tinggi + 1):
        print(" " * (tinggi - i), end="") 
        print("*" * (2 * i - 1))

tinggi = int(input("Masukkan Tinggi Piramida: "))
piramid(tinggi)
print("\n")

# Latihan 2
Data_mahasiswa = {}
jumlah_mahasiswa = int(input("Masukan Jumlah Mahasiswa: "))

for i in range(1, jumlah_mahasiswa + 1):
    nama = input(f"Masukan Nama Mahasiswa ke - {i}: ")
    nilai = int(input(f"Masukan Nilai untuk {nama}: "))
    
    # Menyimpan nilai dalam dictionary dengan nama sebagai key
    Data_mahasiswa[nama] = nilai

print(f"Dictionary = {Data_mahasiswa}")
print("\n")

# Latihan 3
def buat_fileme():
    try:
        nama = input("What's your name? ")
        NIM = input("NIM berapa? ")
        Resolusi = input("Apa resolusi kamu tahun ini? ")

        with open("Me.txt", "w") as file:  # Ubah "W" menjadi "w"
            file.write(f"Nama: {nama}\n")
            file.write(f"NIM: {NIM}\n")
            file.write(f"Resolusi: {Resolusi}\n")
        
        print("File Me.txt telah berhasil dibuat!")

    except Exception as e:
        print(f"Something wrong: {e}")

buat_fileme()
