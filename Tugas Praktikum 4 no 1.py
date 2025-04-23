while True:
    try:
        angka = input("Masukkan angka: ")
        angka = float(angka) 
        if angka < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        elif angka == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
        else:
            result = angka ** 0.5
            print(f"Akar kuadrat dari {angka} adalah {result}")
            break  
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")
