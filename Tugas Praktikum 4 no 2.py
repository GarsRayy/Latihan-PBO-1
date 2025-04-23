def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tambah_tugas(todo_list):
    try:
        tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
        if not tugas:
            raise ValueError("Tugas tidak boleh kosong.")
        todo_list.append(tugas)
        print("Tugas berhasil ditambahkan!")
    except ValueError as ve:
        print(f"Error: {ve}")

def hapus_tugas(todo_list):
    try:
        if not todo_list:
            raise ValueError("Daftar tugas kosong, tidak ada yang bisa dihapus.")

        user_input = input("Masukkan nomor tugas yang ingin dihapus: ").strip()
        indeks = int(user_input) - 1

        if indeks < 0 or indeks >= len(todo_list):
            raise IndexError(f"Tugas dengan nomor {user_input} tidak ditemukan.")

        tugas_terhapus = todo_list.pop(indeks)
        print(f"Tugas '{tugas_terhapus}' berhasil dihapus!")
    except ValueError as ve:
        print(f"Error: Masukkan nomor tugas yang valid. ({ve})")
    except IndexError as ie:
        print(f"Error: {ie}")

def tampilkan_tugas(todo_list):
    if not todo_list:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for i, tugas in enumerate(todo_list, 1):
            print(f"- {tugas}")

def main():
    todo_list = []
    while True:
        tampilkan_menu()
        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            if pilihan not in ('1', '2', '3', '4'):
                raise ValueError("Pilihan tidak valid. Masukkan angka 1-4.")

            if pilihan == '1':
                tambah_tugas(todo_list)
            elif pilihan == '2':
                hapus_tugas(todo_list)
            elif pilihan == '3':
                tampilkan_tugas(todo_list)
            elif pilihan == '4':
                print("Keluar dari program.")
                break
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()
