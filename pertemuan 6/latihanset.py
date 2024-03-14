class TokoPINKY:
    def __init__(self):
        self.keranjang = set()

    def tambah_ke_keranjang(self, barang):
        self.keranjang.add(barang)

    def hapus_dari_keranjang(self, barang):
        self.keranjang.remove(barang)

    def cetak_keranjang(self):
        print("Isi keranjang Anda:")
        for barang in self.keranjang:
            print("-", barang)
    
    def hitung_jumlah_barang(self):
        return len(self.keranjang)

    def update_keranjang(self, barang_lama, barang_baru):
        self.keranjang.remove(barang_lama)
        self.keranjang.add(barang_baru)

# Inisialisasi TokoPINKY
pnky_toko = TokoPINKY()

print("Pelanggan ingin membeli aksesoris di toko PINKY.")

print("\nPelanggan mengambil barang dan memasukkannya ke dalam keranjang.")
pnky_toko.tambah_ke_keranjang("Gelang")
pnky_toko.tambah_ke_keranjang("Kalung")
pnky_toko.tambah_ke_keranjang("Cincin")
pnky_toko.cetak_keranjang()
print("Jumlah barang dalam keranjang:", pnky_toko.hitung_jumlah_barang())

print("\nPelanggan tidak jadi mengambil barang yang diinginkan dan mengambil barang lainnya.")
pnky_toko.hapus_dari_keranjang("Cincin")
pnky_toko.tambah_ke_keranjang("Anting")
pnky_toko.cetak_keranjang()
print("Jumlah barang dalam keranjang:", pnky_toko.hitung_jumlah_barang())

print("\nPelanggan menambahkan barang ke dalam keranjangnya.")
pnky_toko.tambah_ke_keranjang("Topi")
pnky_toko.cetak_keranjang()
print("Jumlah barang dalam keranjang:", pnky_toko.hitung_jumlah_barang())

print("\nPelanggan memutuskan untuk membayar di kasir.")
print("Pelanggan membayar dan keluar dari toko.")

