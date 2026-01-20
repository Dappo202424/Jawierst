import random
import os

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def tampilkan_dadu(nilai):
    """Menampilkan visualisasi dadu dalam ASCII art"""
    dadu_ascii = {
        1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
        ],
        2: [
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"
        ],
        3: [
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"
        ],
        4: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        5: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        6: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"
        ]
    }
    return dadu_ascii.get(nilai, ["Dadu invalid"])

def tampilkan_header():
    """Menampilkan header aplikasi"""
    print("=" * 50)
    print("        🎲 APLIKASI LEMPAR DADU 🎲")
    print("=" * 50)
    print()

def lempar_satu_dadu():
    """Melempar satu dadu"""
    return random.randint(1, 6)

def lempar_banyak_dadu():
    """Melempar multiple dadu"""
    try:
        jumlah = int(input("\nBerapa dadu yang ingin dilempar? (1-10): "))
        
        if jumlah < 1 or jumlah > 10:
            print("❌ Jumlah dadu harus antara 1-10!")
            return None
        
        print(f"\n🎲 Melempar {jumlah} dadu...\n")
        hasil = [lempar_satu_dadu() for _ in range(jumlah)]
        
        # Tampilkan setiap dadu
        max_baris = 5
        for baris in range(max_baris):
            for hasil_dadu in hasil:
                dadu_art = tampilkan_dadu(hasil_dadu)
                print(dadu_art[baris], end="  ")
            print()
        
        total = sum(hasil)
        print(f"\n📊 Hasil dadu: {hasil}")
        print(f"📈 Total: {total}")
        
        return hasil, total
        
    except ValueError:
        print("❌ Input tidak valid! Masukkan angka.")
        return None

def menu_utama():
    """Menu utama aplikasi"""
    while True:
        clear_screen()
        tampilkan_header()
        
        print("Pilihan Menu:")
        print("1. Lempar 1 Dadu")
        print("2. Lempar Banyak Dadu")
        print("3. Keluar")
        print()
        
        pilihan = input("Masukkan pilihan (1-3): ").strip()
        
        if pilihan == '1':
            clear_screen()
            tampilkan_header()
            hasil = lempar_satu_dadu()
            
            # Tampilkan dadu
            print("Hasil Lemparan:")
            print()
            for baris in tampilkan_dadu(hasil):
                print(baris)
            print(f"\n🎯 Anda mendapat: {hasil}")
            
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '2':
            clear_screen()
            tampilkan_header()
            hasil = lempar_banyak_dadu()
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '3':
            clear_screen()
            print("Terima kasih telah menggunakan Aplikasi Dadu! 👋")
            break
        else:
            print("❌ Pilihan tidak valid! Silakan coba lagi.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    menu_utama()
