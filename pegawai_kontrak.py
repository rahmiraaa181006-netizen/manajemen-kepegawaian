from pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Subclass Pegawai untuk karyawan kontrak dengan batas durasi bulan."""

    def __init__(self, nip, nama, email, gaji_pokok, durasi_kontrak_bulan, tunjangan_transport, aktif=True):
        # Memanggil constructor superclass Pegawai menggunakan super()
        super().__init__(nip, nama, email, gaji_pokok, aktif)

        if durasi_kontrak_bulan <= 0 or tunjangan_transport < 0:
            raise ValueError("Durasi kontrak harus positif dan tunjangan tidak boleh negatif")

        # 3 atribut private khusus PegawaiKontrak
        self.__durasi_kontrak_bulan = durasi_kontrak_bulan
        self.__sisa_bulan_kontrak = durasi_kontrak_bulan
        self.__tunjangan_transport = tunjangan_transport

    # --- Getter ---
    def get_durasi_kontrak_bulan(self):
        return self.__durasi_kontrak_bulan

    def get_sisa_bulan_kontrak(self):
        return self.__sisa_bulan_kontrak

    def get_tunjangan_transport(self):
        return self.__tunjangan_transport

    # --- Method khusus dengan validasi ---
    def perpanjang_kontrak(self, tambahan_bulan):
        """Memperpanjang durasi kontrak dan mengaktifkan kembali status jika perlu."""
        if tambahan_bulan <= 0:
            return False
        self.__durasi_kontrak_bulan += tambahan_bulan
        self.__sisa_bulan_kontrak += tambahan_bulan
        self.ubah_status_aktif(True)
        return True

    def catat_bulan_berjalan(self, jumlah_bulan=1):
        """Mengurangi sisa bulan kontrak; otomatis nonaktif jika sisa kontrak habis."""
        if jumlah_bulan <= 0 or jumlah_bulan > self.__sisa_bulan_kontrak:
            return False
        self.__sisa_bulan_kontrak -= jumlah_bulan
        if self.__sisa_bulan_kontrak == 0:
            self.ubah_status_aktif(False)
        return True

    # --- Method tambahan dari Superclass ---
    def get_jenis_pegawai(self):
        return "Pegawai Kontrak"

    def hitung_total_gaji(self):
        """Menghitung total gaji memakai getter publik dari superclass."""
        return self.get_gaji_pokok() + self.__tunjangan_transport

    def tampilkan_info(self):
        """Menampilkan informasi lengkap Pegawai Kontrak."""
        super().tampilkan_info()
        print("Transport  : Rp{:,.0f}".format(self.get_tunjangan_transport()))
        print(f"Kontrak    : Sisa {self.get_sisa_bulan_kontrak()} dari {self.get_durasi_kontrak_bulan()} bulan")