# 🚀 Pitching NetPro: Magang Jaringan
## Visual Novel Edukasi Teknik Komputer & Jaringan (TKJ)

### 📁 Folder Utama
- **`audio/`**: Menyimpan aset suara. Di sini terdapat `bgm_ch1.mp3` untuk suasana kantor dan `bgm_trouble.mp3` yang dipicu saat terjadi krisis jaringan (climax).
- **`gui/`**: Berisi aset gambar untuk antarmuka, seperti tombol "Mulai", "Lanjutkan", dan bingkai kustom yang didesain di Figma.
- **`images/`**: Gudang aset visual utama. Terbagi menjadi `sprites` (karakter Pak Hendra, Rafi, dsb) dan `backgrounds` (Lab, Ruang Server, Kantor).
- **`movies/`**: Menyimpan file video. Contohnya `intro.webm` yang memberikan efek sinematik saat game dimulai (Digital Data Stream Transition).
- **`tl/`**: Singkatan dari *Translation*. Folder ini memungkinkan game NetPro dikonversi ke bahasa lain (misal: Inggris) tanpa mlkengubah kode utama.
- **`saves/`**: Tempat penyimpanan data permainan pemain (Save States).

### 📄 File Kode & Dokumentasi
- **`script.rpy` [INTI]**: Berisi seluruh alur cerita, dialog, dan logika permainan. Semua mekanisme "Quest" edukasi ditulis di sini.
- **`screens.rpy` [UI LOGIC]**: Mengatur tampilan layar. Di sini kita memodifikasi kotak dialog agar bisa berubah menjadi "Mode Terminal" saat kuis berlangsung.
- **`gui_custom.rpy` [DESIGN SYSTEM]**: File kustom untuk mengatur variabel warna neon, style tombol, dan HUD Skor yang tampil di pojok layar.
- **`options.rpy` [CONFIG]**: Mengatur konfigurasi dasar game seperti judul jendela, versi, dan aturan saat proses *build* menjadi aplikasi (.exe).
- **`check_dims.py` [UTILITY]**: Skrip Python pembantu untuk memastikan semua aset gambar memiliki ukuran yang tepat (1920x1080) agar tidak pecah saat dijalankan.


---

## 🛠️ Bedah Kode Terperinci (Technical Walkthrough)

### 1. Logika Interaktif di `script.rpy`
- **Variabel `in_quiz_mode`**: Digunakan sebagai *toggle* (saklar). Jika `True`, maka tampilan game akan berubah total menjadi antarmuka kuis.
- **Fungsi `crimping_check`**: Algoritma pengecekan urutan warna kabel. Menggunakan perbandingan *List* di Python untuk memastikan siswa menyusun kabel UTP standar T568B dengan urutan yang 100% akurat.

### 2. Kustomisasi UI di `screens.rpy`
- **Dynamic Say Screen**: Menggunakan logika `ifgetattr` untuk mendeteksi status kuis. Ini membuktikan bahwa game ini tidak hanya statis, tapi memiliki *state-awareness* (sadar kondisi).

---
