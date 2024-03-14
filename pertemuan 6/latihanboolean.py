#latihan boolean
def hitung_ppn(nilai):
    ppn = nilai * 0.12
    return ppn

def main():
    # Input nilai a dan b
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))

    # Cek apakah a lebih besar dari b
    a_lebih_besar = a > b

    # Cek apakah b lebih besar dari a
    b_lebih_besar = b > a

    # Cek apakah a sama dengan b
    a_sama_dengan_b = a == b

    # Hitung PPN a dan b
    ppn_a = hitung_ppn(a) if a > 10000 else 0
    ppn_b = hitung_ppn(b) if b > 50000 else 0

    # Tambahkan kedua PPN
    total_ppn = ppn_a + ppn_b

    # Output
    print("Apakah a lebih besar dari b?", a_lebih_besar)
    print("Apakah b lebih besar dari a?", b_lebih_besar)
    print("Apakah a sama dengan b?", a_sama_dengan_b)
    print("PPN a:", ppn_a)
    print("PPN b:", ppn_b)
    print("Total PPN:", total_ppn)

    # Hapus a dan b
    del a, b

    # Cek apakah a dan b sudah dihapus
    a_dihapus = "a" not in locals()
    b_dihapus = "b" not in locals()

    # Output setelah penghapusan
    print("Apakah a sudah dihapus?", a_dihapus)
    print("Apakah b sudah dihapus?", b_dihapus)

if __name__ == "__main__":
    main()


