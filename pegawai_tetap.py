from pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Subclass Pegawai untuk karyawan tetap dengan tunjangan dan bonus masa kerja."""

    def __init__(self, nip, nama, email, gaji_pokok, tunjangan_tetap, masa_kerja_tahun, aktif=True):
        # Memanggil constructor superclass Pegawai menggunakan super()
        super().__init__(nip, nama, email, gaji_pokok, aktif)

        if tunjangan_tetap < 0 or masa_kerja_tahun < 0:
            raise ValueError("Tunjangan tetap dan masa kerja tidak boleh negatif")

        # Minimal 3 atribut private khusus PegawaiTetap
        self.__tunjangan_tetap = tunjangan_tetap
        self.__masa_kerja_tahun = masa_kerja_tahun
        self.__bonus_tahunan = 0

    # --- Getter ---
    def get_tunjangan_tetap(self):
        return self.__tunjangan_tetap

    def get_masa_kerja_tahun(self):
        return self.__masa_kerja_tahun

    def get_bonus_tahunan(self):
        return self.__bonus_tahunan

    # --- Method khusus dengan validasi ---
    def ubah_tunjangan_tetap(self, tunjangan_baru):
        """Mengubah nominal tunjangan tetap jika tidak negatif."""
        if tunjangan_baru < 0:
            return False
        self.__tunjangan_tetap = tunjangan_baru
        return True

    # --- Method tambahan dari Superclass ---
    def get_jenis_pegawai(self):
        return "Pegawai Tetap"

    def hitung_total_gaji(self):
        """Menghitung total gaji memakai getter publik dari superclass."""
        return self.get_gaji_pokok() + self.__tunjangan_tetap

    def hitung_bonus_tahunan(self):
        """Menghitung dan menyimpan bonus tahunan berdasarkan lama masa kerja."""
        if self.__masa_kerja_tahun >= 5:
            self.__bonus_tahunan = self.get_gaji_pokok() * 0.5
        elif self.__masa_kerja_tahun >= 2:
            self.__bonus_tahunan = self.get_gaji_pokok() * 0.25
        else:
            self.__bonus_tahunan = 0
        return self.__bonus_tahunan

    def tampilkan_info(self):
        """Menampilkan informasi lengkap Pegawai Tetap."""
        super().tampilkan_info()
        print("Tunjangan  : Rp{:,.0f}".format(self.get_tunjangan_tetap()))
        print("Masa Kerja :", self.get_masa_kerja_tahun(), "tahun")
        print("Bonus Thn  : Rp{:,.0f}".format(self.get_bonus_tahunan()))