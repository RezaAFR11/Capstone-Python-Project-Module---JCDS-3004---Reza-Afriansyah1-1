# 🏥 Data Pasien Rumah Sakit

Merupakan project Capstone Modul 1 Python CRUD JCDS-3004 di Purwadhika.  
Aplikasi berbasis terminal ini berfungsi untuk mencatat, menampilkan, mengubah, dan menghapus data pasien rumah sakit secara interaktif menggunakan Python.

---

## 📌 Fitur Utama

- Melihat semua data pasien
- Mencari data pasien berdasarkan ID atau nama
- Menyaring pasien berdasarkan usia (dewasa/anak-anak)
- Menambahkan data pasien baru
- Mengubah data pasien yang sudah ada
- Menghapus dan memulihkan data pasien
- Menampilkan data dalam bentuk tabel dengan pustaka `tabulate`

---

## 🧱 Struktur Data

Data pasien disimpan dalam format dictionary Python seperti berikut:

```python
list_data_pasien = {
  "PS001": {
    "Nama": "Andi",
    "Umur": 30,
    "Jenis Kelamin": "Laki-laki",
    "Diagnosa": "Demam",
    "Ruangan": "VVIP-001"
  },
  # Data pasien lainnya..
}
```
---
## 📚 Struktur Menu
```python
MENU UTAMA
├── 1. Lihat Data Pasien
│   ├── Lihat Semua
│   ├── Cari Pasien
│   └── Filter Umur
├── 2. Tambah Data Pasien
├── 3. Ubah Data Pasien
├── 4. Hapus Data Pasien
│   ├── Hapus
│   ├── Lihat Data Terhapus
│   └── Pulihkan Data
└── 5. Keluar
```
---
## Kontributor
Proyek ini dikembangkan sebagai bagian dari program pelatihan. Saran dan masukan untuk pengembangan lebih lanjut sangat diterima.
- Nama: Reza Afriansyah
- Kelas: JCDS-3004 Jakarta
- Kegiatan: Capstone Project Module 1 Python
- Mentor: Median Hardiv Nugraha
---
## Catatan
- Terdapat List Data Dummy didalam Program
- Program ini menggunakan input dari console/terminal
- Semua perubahan data bersifat sementara (tidak disimpan ke file/database)
---
## 📄 Lisensi
Proyek ini bebas digunakan untuk keperluan edukatif dan pengembangan pribadi.
