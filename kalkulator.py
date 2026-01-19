def tambah(a, b):
    """Menambahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangi dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka"""
    if b == 0:
        return "Error: Tidak bisa dibagi dengan nol!"
    return a / b

def kalkulator():
    """Fungsi utama kalkulator"""
    print("=" * 40)
    print("    KALKULATOR SIMPEL")
    print("=" * 40)
    print("Pilihan operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    print("=" * 40)
    
    while True:
        pilihan = input("\nPilih operasi (1-5): ").strip()
        
        if pilihan == '5':
            print("\nTerima kasih telah menggunakan kalkulator! Sampai jumpa!")
            break
        
        if pilihan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue
        
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                hasil = tambah(angka1, angka2)
                operasi = "+"
            elif pilihan == '2':
                hasil = kurang(angka1, angka2)
                operasi = "-"
            elif pilihan == '3':
                hasil = kali(angka1, angka2)
                operasi = "*"
            elif pilihan == '4':
                hasil = bagi(angka1, angka2)
                operasi = "/"
            
            print(f"\nHasil: {angka1} {operasi} {angka2} = {hasil}")
            
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    kalkulator()
