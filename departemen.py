class Departemen:
    """Class relasi Association: satu Departemen memiliki satu atau lebih Pegawai."""

    def __init__(self, kode_dept, nama_dept, lokasi):
        if not kode_dept or not nama_dept:
            raise ValueError("Kode dan nama departemen tidak boleh kosong")

        # 3 atribut private
        self.__kode_dept = kode_dept
        self.__nama_dept = nama_dept
        self.__lokasi = lokasi
        self.__daftar_pegawai = []

    # --- Getter ---
    def get_kode_dept(self):
        return self.__kode_dept

    def get_nama_dept(self):
        return self.__nama_dept

    def get_lokasi(self):
        return self.__lokasi

    def get_daftar_pegawai(self):
        """Mengembalikan salinan list agar __daftar_pegawai tidak diubah langsung dari luar."""
        return list(self.__daftar_pegawai)

    # --- Method tambahan pada Departemen ---
    def tambah_pegawai(self, pegawai):
        """Menambahkan objek Pegawai ke departemen (menolak jika NIP sudah ada)."""
        if self.cari_pegawai_by_nip(pegawai.get_nip()) is not None:
            return False
        self.__daftar_pegawai.append(pegawai)
        return True

    def cari_pegawai_by_nip(self, nip):
        """Mencari satu objek Pegawai berdasarkan NIP."""
        for pegawai in self.__daftar_pegawai:
            if pegawai.get_nip().lower() == nip.lower():
                return pegawai
        return None

    def cari_pegawai_by_nama(self, kata_kunci):
        """Mencari daftar Pegawai yang namanya mengandung kata kunci."""
        hasil = []
        kunci = kata_kunci.lower()
        for pegawai in self.__daftar_pegawai:
            if kunci in pegawai.get_nama().lower():
                hasil.append(pegawai)
        return hasil

    def hitung_total_anggaran_gaji(self):
        """Menghitung total pengeluaran gaji seluruh pegawai aktif di departemen."""
        total = 0
        for pegawai in self.__daftar_pegawai:
            if pegawai.is_aktif():
                total += pegawai.hitung_total_gaji()
        return total