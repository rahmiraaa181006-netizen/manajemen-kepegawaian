class Pegawai:
    """Superclass yang merepresentasikan entitas dasar Pegawai."""

    def __init__(self, nip, nama, email, gaji_pokok, aktif=True):
        # Validasi nilai awal pada constructor 
        if not nip or not nama:
            raise ValueError("NIP dan nama pegawai tidak boleh kosong")
        if gaji_pokok < 0:
            raise ValueError("Gaji pokok tidak boleh negatif")

        # 3 atribut private 
        self.__nip = nip
        self.__nama = nama
        self.__email = ""
        self.__gaji_pokok = gaji_pokok
        self.__aktif = aktif

        # Menggunakan method ubah_email() agar validasi email langsung diterapkan
        if not self.ubah_email(email):
            raise ValueError("Format email awal tidak valid (harus mengandung '@' dan '.')")

    # --- Getter untuk membaca atribut private ---
    def get_nip(self):
        return self.__nip

    def get_nama(self):
        return self.__nama

    def get_email(self):
        return self.__email

    def get_gaji_pokok(self):
        return self.__gaji_pokok

    def is_aktif(self):
        return self.__aktif

    # --- Method khusus dengan validasi  ---
    def ubah_nama(self, nama_baru):
        """Mengubah nama pegawai jika tidak kosong."""
        if not nama_baru or not nama_baru.strip():
            return False
        self.__nama = nama_baru.strip()
        return True

    def ubah_email(self, email_baru):
        """Mengubah email hanya jika format dasar valid ('@' dan '.')."""
        if "@" not in email_baru or "." not in email_baru:
            return False
        self.__email = email_baru.strip()
        return True

    def ubah_gaji_pokok(self, gaji_baru):
        """Mengubah gaji pokok hanya jika bernilai positif."""
        if gaji_baru <= 0:
            return False
        self.__gaji_pokok = gaji_baru
        return True

    def ubah_status_aktif(self, status_baru):
        """Mengubah status aktif/nonaktif pegawai."""
        if not isinstance(status_baru, bool):
            return False
        self.__aktif = status_baru
        return True

    # --- Method tambahan pada Superclass ---
    def get_jenis_pegawai(self):
        return "Pegawai Umum"

    def hitung_total_gaji(self):
        """Menghitung total gaji dasar (akan di-override oleh subclass)."""
        return self.__gaji_pokok

    def get_label_status(self):
        """Mengembalikan teks status kepegawaian."""
        return "Aktif" if self.__aktif else "Tidak Aktif"

    def tampilkan_info(self):
        """Menampilkan informasi dasar pegawai ke layar."""
        print("NIP        :", self.get_nip())
        print("Nama       :", self.get_nama())
        print("Jenis      :", self.get_jenis_pegawai())
        print("Email      :", self.get_email())
        print("Gaji Pokok : Rp{:,.0f}".format(self.get_gaji_pokok()))
        print("Total Gaji : Rp{:,.0f}".format(self.hitung_total_gaji()))
        print("Status     :", self.get_label_status())