from departemen import Departemen
from pegawai_tetap import PegawaiTetap
from pegawai_kontrak import PegawaiKontrak


def muat_data_awal(departemen):
    """Membuat beberapa object awal agar aplikasi langsung siap diuji."""
    p1 = PegawaiTetap("PGW01", "Rina Kusuma", "rina@perusahaan.com", 8000000, 1500000, 6)
    p2 = PegawaiTetap("PGW02", "Budi Santoso", "budi@perusahaan.com", 6500000, 1000000, 2)
    p3 = PegawaiKontrak("PGW03", "Dewi Lestari", "dewi@perusahaan.com", 5000000, 12, 750000)

    # method perhitungan bonus awal
    p1.hitung_bonus_tahunan()
    p2.hitung_bonus_tahunan()

    departemen.tambah_pegawai(p1)
    departemen.tambah_pegawai(p2)
    departemen.tambah_pegawai(p3)


def menu_tambah_data(departemen):
    """Menu 1: Menambah data Pegawai Tetap atau Pegawai Kontrak."""
    print("\n--- TAMBAH DATA PEGAWAI ---")
    print("1. Pegawai Tetap")
    print("2. Pegawai Kontrak")
    jenis = input("Pilih jenis pegawai (1/2): ").strip()

    if jenis not in ("1", "2"):
        print("Pilihan jenis tidak valid.")
        return

    nip = input("Masukkan NIP (contoh: PGW04): ").strip()
    if departemen.cari_pegawai_by_nip(nip) is not None:
        print(f"Gagal: NIP '{nip}' sudah terdaftar.")
        return

    nama = input("Masukkan Nama Lengkap: ").strip()
    email = input("Masukkan Email: ").strip()

    try:
        gaji_pokok = float(input("Masukkan Gaji Pokok (Rp): ").strip())
        if jenis == "1":
            tunjangan = float(input("Masukkan Tunjangan Tetap (Rp): ").strip())
            masa_kerja = int(input("Masukkan Masa Kerja (tahun): ").strip())
            pegawai_baru = PegawaiTetap(nip, nama, email, gaji_pokok, tunjangan, masa_kerja)
            pegawai_baru.hitung_bonus_tahunan()
        else:
            durasi = int(input("Masukkan Durasi Kontrak (bulan): ").strip())
            transport = float(input("Masukkan Tunjangan Transport (Rp): ").strip())
            pegawai_baru = PegawaiKontrak(nip, nama, email, gaji_pokok, durasi, transport)

        if departemen.tambah_pegawai(pegawai_baru):
            print(f"Berhasil menambahkan '{pegawai_baru.get_nama()}' ke {departemen.get_nama_dept()}.")
        else:
            print("Gagal menambahkan data pegawai.")
    except ValueError as err:
        print(f"Input tidak valid: {err}")


def menu_tampilkan_data(departemen):
    """Menu 2: Menampilkan seluruh data pegawai di dalam departemen."""
    print("\n==================================================")
    print(f" DAFTAR PEGAWAI - {departemen.get_nama_dept().upper()} ({departemen.get_lokasi()})")
    print("==================================================")

    daftar = departemen.get_daftar_pegawai()
    if not daftar:
        print("Belum ada data pegawai.")
        return

    for nomor, pegawai in enumerate(daftar, start=1):
        print(f"\n[{nomor}]")
        pegawai.tampilkan_info()
        print("-" * 50)

    print("Total Anggaran Gaji Aktif : Rp{:,.0f}".format(departemen.hitung_total_anggaran_gaji()))


def menu_cari_data(departemen):
    """Menu 3: Mencari data pegawai berdasarkan NIP atau Nama."""
    print("\n--- CARI DATA PEGAWAI ---")
    print("1. Cari berdasarkan NIP")
    print("2. Cari berdasarkan Nama")
    pilihan = input("Pilih metode pencarian (1/2): ").strip()

    if pilihan == "1":
        nip = input("Masukkan NIP yang dicari: ").strip()
        pegawai = departemen.cari_pegawai_by_nip(nip)
        if pegawai is not None:
            print("\nData ditemukan:")
            pegawai.tampilkan_info()
        else:
            print("Pegawai dengan NIP tersebut tidak ditemukan.")
    elif pilihan == "2":
        nama = input("Masukkan kata kunci Nama: ").strip()
        hasil_list = departemen.cari_pegawai_by_nama(nama)
        if hasil_list:
            print(f"\nDitemukan {len(hasil_list)} pegawai:")
            for pegawai in hasil_list:
                print("-" * 40)
                pegawai.tampilkan_info()
        else:
            print("Tidak ada pegawai dengan nama tersebut.")
    else:
        print("Pilihan pencarian tidak valid.")


def menu_ubah_data(departemen):
    """Menu 4: Mengubah atribut pegawai melalui method enkapsulasi."""
    print("\n--- UBAH DATA PEGAWAI ---")
    nip = input("Masukkan NIP pegawai yang akan diubah: ").strip()
    pegawai = departemen.cari_pegawai_by_nip(nip)

    if pegawai is None:
        print("Pegawai tidak ditemukan.")
        return

    print("\nData saat ini:")
    pegawai.tampilkan_info()

    print("\nPilih data yang ingin diubah:")
    print("1. Ubah Nama")
    print("2. Ubah Email")
    print("3. Ubah Gaji Pokok")
    print("4. Ubah Status Aktif/Nonaktif")
    if isinstance(pegawai, PegawaiKontrak):
        print("5. Perpanjang Kontrak (bulan)")
        print("6. Catat Bulan Berjalan Kontrak")

    opsi = input("Masukkan pilihan: ").strip()

    if opsi == "1":
        nama_baru = input("Masukkan Nama baru: ").strip()
        print("Berhasil diubah." if pegawai.ubah_nama(nama_baru) else "Gagal: Nama tidak valid.")
    elif opsi == "2":
        email_baru = input("Masukkan Email baru: ").strip()
        print("Berhasil diubah." if pegawai.ubah_email(email_baru) else "Gagal: Format email salah.")
    elif opsi == "3":
        try:
            gaji_baru = float(input("Masukkan Gaji Pokok baru (Rp): ").strip())
            if pegawai.ubah_gaji_pokok(gaji_baru):
                if isinstance(pegawai, PegawaiTetap):
                    pegawai.hitung_bonus_tahunan()
                print("Gaji pokok berhasil diperbarui.")
            else:
                print("Gagal: Gaji harus lebih besar dari 0.")
        except ValueError:
            print("Input gaji harus berupa angka.")
    elif opsi == "4":
        status_input = input("Set status (1 = Aktif, 2 = Tidak Aktif): ").strip()
        if status_input == "1":
            pegawai.ubah_status_aktif(True)
            print("Status diubah menjadi Aktif.")
        elif status_input == "2":
            pegawai.ubah_status_aktif(False)
            print("Status diubah menjadi Tidak Aktif.")
        else:
            print("Pilihan status tidak valid.")
    elif opsi == "5" and isinstance(pegawai, PegawaiKontrak):
        try:
            tambahan = int(input("Tambah durasi kontrak (bulan): ").strip())
            if pegawai.perpanjang_kontrak(tambahan):
                print(f"Kontrak diperpanjang. Sisa kontrak: {pegawai.get_sisa_bulan_kontrak()} bulan.")
            else:
                print("Gagal: Tambahan bulan harus positif.")
        except ValueError:
            print("Input harus berupa angka bulat.")
    elif opsi == "6" and isinstance(pegawai, PegawaiKontrak):
        try:
            bulan = int(input("Jumlah bulan kontrak yang sudah berjalan: ").strip())
            if pegawai.catat_bulan_berjalan(bulan):
                print(f"Sisa kontrak: {pegawai.get_sisa_bulan_kontrak()} bln | Status: {pegawai.get_label_status()}")
            else:
                print("Gagal: Jumlah bulan melebihi sisa kontrak atau tidak valid.")
        except ValueError:
            print("Input harus berupa angka bulat.")
    else:
        print("Opsi tidak tersedia.")


def menu_cek_status_data(departemen):
    """Menu 5: Mengecek status kepegawaian dan detail masa kerja / sisa kontrak."""
    print("\n--- CEK STATUS DATA PEGAWAI ---")
    nip = input("Masukkan NIP : ").strip()

    if nip:
        pegawai = departemen.cari_pegawai_by_nip(nip)
        if pegawai is None:
            print("Pegawai tidak ditemukan.")
            return
        daftar_cek = [pegawai]
    else:
        daftar_cek = departemen.get_daftar_pegawai()

    if not daftar_cek:
        print("Tidak ada data pegawai.")
        return

    for pegawai in daftar_cek:
        ringkasan = (
            f"[{pegawai.get_nip()}] {pegawai.get_nama()} | "
            f"{pegawai.get_jenis_pegawai()} | Status: {pegawai.get_label_status()}"
        )
        if isinstance(pegawai, PegawaiTetap):
            ringkasan += f" | Masa Kerja: {pegawai.get_masa_kerja_tahun()} thn | Bonus: Rp{pegawai.get_bonus_tahunan():,.0f}"
        elif isinstance(pegawai, PegawaiKontrak):
            ringkasan += f" | Sisa Kontrak: {pegawai.get_sisa_bulan_kontrak()}/{pegawai.get_durasi_kontrak_bulan()} bln"
        print(ringkasan)


def main():
    """Fungsi utama untuk menjalankan aplikasi CLI."""
    # Membuat object Departemen (Relasi Association dengan Pegawai)
    dept_it = Departemen("DEPT-01", "Teknologi Informasi", "Gedung A Lantai 3")
    muat_data_awal(dept_it)

    while True:
        print("\n==============================================")
        print("    APLIKASI MANAJEMEN KEPEGAWAIAN (CLI)")
        print("==============================================")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Cari data")
        print("4. Ubah data")
        print("5. Cek status data")
        print("6. Keluar dari program")
        print("----------------------------------------------")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            menu_tambah_data(dept_it)
        elif pilihan == "2":
            menu_tampilkan_data(dept_it)
        elif pilihan == "3":
            menu_cari_data(dept_it)
        elif pilihan == "4":
            menu_ubah_data(dept_it)
        elif pilihan == "5":
            menu_cek_status_data(dept_it)
        elif pilihan == "6":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-6.")


if __name__ == "__main__":
    main()