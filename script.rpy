## ============================================================
## NetPro: Magang Jaringan
## Visual Novel Edukasi Teknik Komputer & Jaringan (TKJ)
## Versi 1.0 | Siap Dikembangkan Komersial
## ============================================================

## ─── DEFINISI KARAKTER ────────────────────────────────────────

define mc     = Character("[nama_mc]", color="#00E5FF", what_color="#FFFFFF")
define mentor = Character("Pak Hendra", color="#FFD700", what_color="#FFD700")
define rafi   = Character("Rafi",       color="#76FF03", what_color="#76FF03")
define client = Character("Bu Dewi",    color="#FF80AB", what_color="#FF80AB")
define admin  = Character("Pak Admin",  color="#FF6E40", what_color="#FF6E40")
define sistem = Character("[[ SISTEM ]]", color="#B0BEC5", what_color="#B0BEC5")
define narasi = Character("",          color="#CFD8DC", what_color="#E0E0E0", what_italic=True)

## ─── VARIABEL GAME ────────────────────────────────────────────

default score          = 0
default tries_q1       = 0
default tries_q2       = 0
default tries_q3       = 0
default tries_climax   = 0
default nama_mc        = "Alex"
default refleksi_score = 0
default ch2_score      = 0
default tries_ch2_q1   = 0
default tries_ch2_q2   = 0
default tries_ch2_q3   = 0
default tries_ch2_climax = 0

## ─── VARIABEL MINI-GAME CRIMPING ──────────────────────────────
## Urutan T568B yang benar: OW, O, GW, BL, BLW, G, CW, C

default crimping_slot  = [0, 0, 0, 0, 0, 0, 0, 0]
## ─── PENYESUAIAN POSISI & UKURAN KARAKTER ────────────────────
## Menarik posisi kiri/kanan lebih ke pinggir agar tidak menumpuk di tengah
transform left:
    xpos 0.25
    xanchor 0.5

transform right:
    xpos 0.75
    xanchor 0.5

transform center:
    xpos 0.5
    xanchor 0.5
    
transform loncat:
    easein 0.15 yoffset -40
    easeout 0.15 yoffset 0
    easein 0.1 yoffset -20
    easeout 0.1 yoffset 0

## Menyesuaikan ukuran semua gambar agar pas di layar (Zoom 0.65, nempel bawah)

image mentor neutral = Transform("images/mentor neutral.png", zoom=0.65, yalign=1.0)
image mentor tegas   = Transform("images/mentor tegas.png", zoom=0.65, yalign=1.0)
image mentor senyum  = Transform("images/mentor senyum.png", zoom=0.65, yalign=1.0)

image rafi neutral   = Transform("images/rafi neutral.png", zoom=0.65, yalign=1.0)
image rafi bingung   = Transform("images/rafi bingung.png", zoom=0.65, yalign=1.0)
image rafi malu      = Transform("images/rafi malu.png", zoom=0.65, yalign=1.0)

image client neutral = Transform("images/client neutral.png", zoom=0.65, yalign=1.0)
image client panik   = Transform("images/client panik.png", zoom=0.65, yalign=1.0)

image admin neutral  = Transform("images/admin neutral.png", zoom=0.65, yalign=1.0)
image admin serius   = Transform("images/admin serius.png", zoom=0.65, yalign=1.0)
image admin happy    = Transform("images/admin happy.png", zoom=0.65, yalign=1.0)

# Definisi video intro sebagai Movie displayable agar bisa pakai transition
image intro_movie = Transform(Movie(play="movies/intro.webm", loop=False, last_frame="images/bg luar.jpg"), size=(1920, 1080))

# Definisi Background agar pas selayar (1920x1080) dan tidak terpotong
image bg luar   = Transform("images/bg luar.jpg", size=(1920, 1080))
image bg kantor = Transform("images/bg kantor.jpg", size=(1920, 1080))
image bg lab    = Transform("images/bg lab.jpg", size=(1920, 1080))
image bg serverroom = Transform("images/bg serverroom.jpg", size=(1920, 1080))

## ─── FUNGSI PYTHON HELPER ─────────────────────────────────────

init python:

    def get_grade():
        """Mengembalikan grade berdasarkan score."""
        if score >= 80:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 40:
            return "C"
        else:
            return "D"

    def get_ending_type():
        if score >= 70:
            return "pro"
        elif score >= 40:
            return "mid"
        else:
            return "bad"

    def crimping_check(slots):
        """Periksa apakah urutan crimping T568B sudah benar."""
        correct = [1, 2, 3, 4, 5, 6, 7, 8]
        return slots == correct

## ─── LAYAR KUSTOM ─────────────────────────────────────────────

## HUD Score
screen hud_score():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 10
        background Frame("#1A237E88", 8, 8)
        padding (12, 8)
        vbox:
            spacing 2
            text "[[ SKOR ]]" size 11 color "#90CAF9" xalign 1.0
            text "[score] poin" size 18 color "#E3F2FD" bold True xalign 1.0

## Layar konfirmasi pilihan
screen konfirmasi(pesan, label_ya, label_tidak):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        background Frame("#12192B", 12, 12)
        padding (30, 20)
        vbox:
            spacing 15
            text pesan size 20 color "#E3F2FD" xalign 0.5
            hbox:
                spacing 20
                xalign 0.5
                textbutton "Ya"    action [Hide("konfirmasi"), Jump(label_ya)] style "choice_button"
                textbutton "Tidak" action [Hide("konfirmasi"), Jump(label_tidak)] style "choice_button"

## Layar mini-game crimping
screen crimping_game():
    modal True

    ## Background panel
    frame:
        xalign 0.5
        yalign 0.5
        xsize 780
        background Frame("#0D1117", 16, 16)
        padding (24, 20)

        vbox:
            spacing 12

            ## Judul
            text "🔌 MINI-GAME: CRIMPING T568B" size 22 color "#00E5FF" bold True xalign 0.5

            ## Instruksi
            text "Susun urutan warna kabel UTP standar T568B dengan benar!" size 13 color "#B0BEC5" xalign 0.5

            null height 5

            ## Referensi standar
            frame:
                background Frame("#0A1628", 8, 8)
                padding (12, 8)
                vbox:
                    text "[[ Urutan Standar T568B ]]:" size 12 color "#78909C" bold True
                    hbox:
                        spacing 4
                        for i, nama in enumerate(["1.Pt.Orange", "2.Orange", "3.Pt.Hijau", "4.Biru", "5.Pt.Biru", "6.Hijau", "7.Pt.Coklat", "8.Coklat"]):
                            frame:
                                background Frame(kabel_warna_bg(i+1), 4, 4)
                                padding (6, 4)
                                text nama size 10 color "#FFFFFF" bold True

            null height 8

            ## Grid slot — tampilkan urutan yang sudah diisi
            text "Klik warna kabel sesuai urutan (1 → 8):" size 13 color "#E3F2FD"

            hbox:
                spacing 6
                xalign 0.5
                for i in range(8):
                    vbox:
                        spacing 4
                        frame:
                            xsize 72
                            ysize 40
                            background Frame(slot_color(crimping_slot[i]), 4, 4)
                            text (slot_label(crimping_slot[i]) if crimping_slot[i] != 0 else "?") size 11 color "#FFFFFF" bold True xalign 0.5 yalign 0.5
                        text str(i+1) size 12 color "#B0BEC5" xalign 0.5

            null height 6

            ## Panel pilih kabel — klik langsung isi slot berikutnya
            frame:
                background Frame("#0A1628", 8, 8)
                padding (10, 8)
                vbox:
                    spacing 6
                    text "Pilih warna kabel:" size 12 color "#78909C"
                    hbox:
                        spacing 4
                        xalign 0.5
                        vbox:
                            spacing 4
                            for row_start in [0, 4]:
                                hbox:
                                    spacing 4
                                    for i in range(row_start, row_start + 4):
                                        textbutton slot_label(i+1):
                                            xsize 84
                                            background Frame(kabel_warna_bg(i+1), 4, 4)
                                            text_color "#FFFFFF"
                                            text_size 10
                                            text_bold True
                                            action Function(add_kabel_to_next_slot, i+1)

            ## Tombol aksi
            null height 6
            hbox:
                spacing 12
                xalign 0.5
                textbutton "🔄 Reset":
                    action [
                        SetVariable("crimping_slot", [0,0,0,0,0,0,0,0]),
                    ]
                    background Frame("#B71C1C", 6, 6)
                    text_color "#EF9A9A"
                    text_size 13

                textbutton "⌫ Hapus":
                    action Function(hapus_slot_terakhir)
                    background Frame("#E65100", 6, 6)
                    text_color "#FFE0B2"
                    text_size 13

                textbutton "✔ Cek Jawaban":
                    action [Hide("crimping_game"), Return("check")]
                    background Frame("#0D47A1", 6, 6)
                    text_color "#90CAF9"
                    text_size 13

## Layar hasil crimping
screen crimping_result(benar):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        background Frame(("#0D3B0D" if benar else "#3B0D0D"), 16, 16)
        padding (30, 24)
        vbox:
            spacing 12
            text ("✅ CRIMPING BERHASIL!" if benar else "❌ URUTAN SALAH!") size 24 color ("#76FF03" if benar else "#FF5252") bold True xalign 0.5
            text ("Urutan T568B kamu sudah benar. Kabel siap digunakan!" if benar else "Urutan kabel belum sesuai standar T568B.\nCoba lagi dengan hati-hati!") size 15 color "#E0E0E0" xalign 0.5
            null height 8
            textbutton "OK":
                xalign 0.5
                action Hide("crimping_result")
                background Frame(("#1B5E20" if benar else "#B71C1C"), 8, 8)
                text_color "#FFFFFF"
                text_bold True

## ─── PYTHON HELPER UNTUK LAYAR ────────────────────────────────

init python:

    _kabel_names = {
        0: "?",
        1: "Pt.Orange",  # Putih Orange
        2: "Orange",     # Orange
        3: "Pt.Hijau",   # Putih Hijau
        4: "Biru",       # Biru
        5: "Pt.Biru",    # Putih Biru
        6: "Hijau",      # Hijau
        7: "Pt.Coklat",  # Putih Coklat
        8: "Coklat",     # Coklat
    }

    _kabel_colors = {
        0: "#37474F",
        1: "#FFB74D",  # Orange Putih (emas muda)
        2: "#FF7043",  # Orange
        3: "#AED581",  # Hijau Putih
        4: "#42A5F5",  # Biru
        5: "#29B6F6",  # Biru Putih (cyan)
        6: "#66BB6A",  # Hijau
        7: "#A1887F",  # Coklat Putih
        8: "#795548",  # Coklat
    }

    def slot_label(val):
        return _kabel_names.get(val, "?")

    def slot_color(val):
        return _kabel_colors.get(val, "#37474F")

    def kabel_warna_bg(idx):
        return _kabel_colors.get(idx, "#37474F")

    def add_kabel_to_next_slot(kabel_idx):
        """Isi slot berikutnya yang masih kosong dengan warna yang dipilih."""
        for i in range(8):
            if crimping_slot[i] == 0:
                crimping_slot[i] = kabel_idx
                break

    def hapus_slot_terakhir():
        """Hapus warna pada slot terakhir yang terisi."""
        for i in range(7, -1, -1):
            if crimping_slot[i] != 0:
                crimping_slot[i] = 0
                break

    def check_crimping():
        correct = [1, 2, 3, 4, 5, 6, 7, 8]
        return list(crimping_slot) == correct

## ============================================================
## ─── SPLASHSCREEN (Video di Awal Game) ──────────────────────
## ============================================================

label splashscreen:
    return

## ============================================================
## ─── LABEL START (Titik Masuk) ─────────────────────────────
## ============================================================


label start:
    # Sembunyikan window dialog
    window hide

    # Mulai dengan layar hitam
    scene black

    # Fade In Video (Tersedot ke portal)
    show intro_movie with dissolve

    # Sesuaikan angka ini dengan durasi video kamu
    $ renpy.pause(10.0)

    # Fade Out Video
    hide intro_movie with dissolve

    # --- BAGIAN DIALOG BINGUNG ---
    # Tampilkan teks di layar hitam dulu untuk kesan misterius
    narasi "Ugh... kepalaku... sakit sekali..."
    narasi "Apa yang baru saja terjadi?"
    narasi "Rasanya seperti seluruh badanku ditarik paksa ke dalam lubang cahaya tadi..."

    ## Setup Latar dan Musik
    play music "audio/bgm_main.mp3" fadein 1.5
    scene bg luar with dissolve
    
    narasi "Tunggu... bukannya tadi aku sedang berdiri di depan rak server di laboratorium?"
    narasi "Kenapa sekarang aku malah ada di depan gedung PT. Nusanet?"
    narasi "Apakah itu tadi cuma mimpi? Tapi rasanya sangat nyata..."

    narasi "Selamat Datang di NetPro: Magang Jaringan!"
    narasi "Sebelum memulai petualanganmu, tentukan namamu terlebih dahulu."

    ## Input Nama Pemain
    $ nama_mc = renpy.input("Siapa nama kamu?", default="Alex").strip()
    
    if not nama_mc:
        $ nama_mc = "Alex"

    # Reset variabel game
    $ score          = 0
    $ crimping_slot  = [0,0,0,0,0,0,0,0]

    show screen hud_score

    narasi "Kamu mencoba menenangkan diri dan merapikan seragam magangmu."
    narasi "Hari ini adalah hari pertama magangmu di divisi IT, namun kejadian di 'mimpi' tadi masih membekas."

    jump intro

## ============================================================
## ─── ACT 1: INTRO ──────────────────────────────────────────
## ============================================================

label intro:

    scene bg kantor with dissolve

    narasi "Kamu memasuki ruang IT yang dipenuhi kabel, switch, dan monitor."

    show mentor neutral at right with dissolve
    mentor "Hei, kamu pasti [nama_mc] yang baru?"
    mc "Iya, Pak. Saya [nama_mc]. Senang bisa magang di sini!"
    mentor "Nama saya Hendra. Senior teknisi di sini. Panggil saja Pak Hendra."
    mentor "Di sini kita tidak bisa santai. Jaringan mati = operasional berhenti."
    mentor "Tapi jangan takut — saya akan bimbing kamu step by step."

    show rafi neutral at left with dissolve
    rafi "Oi! Nama gue Rafi. Sesama anak magang. Kita bakal jadi rekan kerja nih!"
    mc "Haha, oke Rafi! Siap kerjasama."
    rafi "Btw, kata senior sebelumnya: kalau nggak ngerti, pura-pura ngerti aja dulu. 😁"

    show mentor tegas at right with vpunch
    mentor "Rafi... itu nasihat yang sangat salah."
    rafi "E-eh, bercanda Pak! Hehehe..."

    hide rafi with dissolve

    mentor "Baik [nama_mc], kita mulai dari dasar. Ikuti saya ke lab jaringan."

    hide mentor with dissolve
    scene bg lab with dissolve

    narasi "Ruang laboratorium jaringan. Baris demi baris switch, patch panel, dan server rack berjejer rapi."
    narasi "Aroma kabel dan udara dingin dari AC terasa familiar — inilah dunia IT yang sesungguhnya."

    show mentor neutral at right with dissolve
    mentor "Ini lab utama kami. Semua infrastruktur jaringan kantor dikendalikan dari sini."
    mentor "Kamu akan belajar langsung dari case nyata. Siap?"

    menu:
        "Siap, Pak! Saya tidak sabar untuk mulai belajar.":
            $ score += 5
            mc "Siap, Pak! Saya sudah pelajari dasar-dasarnya sedikit. Siap untuk praktek!"
            show mentor senyum at right, loncat
            mentor "Bagus! Semangat itu yang kita butuhkan."

        "Jujur saja... saya masih banyak yang belum tahu, Pak.":
            mc "Jujur Pak, saya masih banyak yang belum tahu. Tapi saya mau belajar!"
            show mentor tegas
            mentor "Kejujuran itu bagus. Lebih baik jujur dari pada sok tahu dan bikin jaringan down."

    mentor "Quest pertama sudah menunggu. Yuk kita mulai."

    jump quest1

## ============================================================
## ─── ACT 2: TRAINING ────────────────────────────────────────
## ============================================================

## ─── QUEST 1: JENIS KABEL ───────────────────────────────────

label quest1:

    scene bg lab with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ QUEST 1: MENGHUBUNGKAN PC KE SWITCH ═══"

    mentor "Quest pertama: kamu harus menghubungkan sebuah PC workstation ke switch jaringan."
    mentor "Pertanyaannya: kabel UTP jenis apa yang kamu gunakan?"

    show rafi bingung at left, loncat with dissolve
    rafi "Eh, bukannya asal colok aja bisa? Kabel kan ya kabel..."
    mentor "SALAH. Jenis kabel menentukan apakah koneksi berhasil atau tidak."

    hide rafi with dissolve

    mentor "Ada dua opsi: Straight-through atau Crossover. Pilih dengan cermat!"

    narasi "[[ Koneksi: PC ──── Switch ]]"

label quest1_pilih:

    $ tries_q1 += 1

    menu:
        "Kabel Straight-through (T568B ke T568B)":
            jump quest1_benar

        "Kabel Crossover (T568A ke T568B)":
            jump quest1_salah

label quest1_benar:

    $ score += 20
    scene bg lab with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve

    sistem "[[ PING 8.8.8.8 ]] → Reply from 8.8.8.8: bytes=32 time=1ms TTL=128"
    sistem "[[ STATUS ]] ✅ CONNECTED — Koneksi berhasil!"

    mentor "Tepat sekali! Kabel Straight-through digunakan untuk menghubungkan perangkat BERBEDA jenis."
    mentor "PC ke Switch, PC ke Hub, Switch ke Router — semuanya pakai Straight-through."
    mc "Oh jadi kalau perangkat sama (PC ke PC atau Switch ke Switch) baru pakai Crossover ya?"
    mentor "Persis! Sekarang kamu sudah mengerti. +20 poin untuk kamu."

    narasi "─── PENJELASAN TEKNIS ───"
    narasi "Straight-through: kedua ujung pin 1-8 identik (T568B ke T568B atau T568A ke T568A)"
    narasi "Crossover: satu ujung T568A, ujung lain T568B — pin TX dan RX di-swap"
    narasi "Modern: Banyak switch/NIC modern sudah support Auto-MDI/MDI-X, bisa deteksi otomatis"

    jump quest2

label quest1_salah:

    scene bg lab with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    sistem "[[ PING 8.8.8.8 ]] → Request Timed Out"
    sistem "[[ STATUS ]] ❌ RTO — Tidak ada respon!"

    mentor "Kabel Crossover digunakan untuk menghubungkan perangkat SEJENIS."
    mentor "PC ke PC, Switch ke Switch — itu Crossover. PC ke Switch? Straight-through!"
    mc "Oh... saya salah. Maaf Pak."
    mentor "Tidak apa-apa. Coba lagi, dan kali ini pikirkan dulu jenis perangkatnya."

    if tries_q1 >= 3:
        mentor "Sudah tiga kali coba. Ingat baik-baik: perangkat berbeda → Straight-through."
        mentor "Saya bantu: PC dan Switch adalah perangkat BERBEDA jenis. Jadi..."
        jump quest1_pilih
    else:
        jump quest1_pilih

## ─── QUEST 2: CRIMPING T568B ────────────────────────────────

label quest2:

    scene bg lab with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ QUEST 2: MINI-GAME CRIMPING KABEL T568B ═══"

    mentor "Quest berikutnya: kita akan membuat kabel UTP dari awal — proses crimping!"
    mentor "Kabel UTP memiliki 8 kawat dengan warna berbeda. Urutan pemasangan harus TEPAT."
    mentor "Standar yang kita gunakan adalah T568B. Hafalkan ini baik-baik!"

    narasi "─── STANDAR T568B ───"
    narasi "Pin 1: Putih Orange"
    narasi "Pin 2: Orange"
    narasi "Pin 3: Putih Hijau"
    narasi "Pin 4: Biru"
    narasi "Pin 5: Putih Biru"
    narasi "Pin 6: Hijau"
    narasi "Pin 7: Putih Coklat"
    narasi "Pin 8: Coklat"

    show rafi neutral at left with dissolve
    rafi "Gue coba inget urutannya: Orange dulu, terus Hijau, terus Biru, terus Coklat. Tiap warna didahului Putih kecuali yang asli."
    mentor "Betul! Cara gampangnya: ingat 4 warna utama — Orange, Hijau, Biru, Coklat. Setiap pasangnya dimulai dari Putih dulu. Sekarang [nama_mc], giliranmu!"
    hide rafi with dissolve

    mentor "Susun urutan 8 kabel sesuai standar T568B. Gunakan panel di bawah ini."

label quest2_mulai:

    $ tries_q2 += 1
    $ crimping_slot = [0,0,0,0,0,0,0,0]

    call screen crimping_game

    if check_crimping():
        jump quest2_benar
    else:
        jump quest2_salah

label quest2_benar:

    $ score += 25
    scene bg lab with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve

    sistem "[[ CABLE TEST ]] ✅ T568B — Semua 8 pin terhubung dengan benar!"
    sistem "[[ HASIL ]] Benar — Putih Orange, Orange, Putih Hijau, Biru, Putih Biru, Hijau, Putih Coklat, Coklat ✓"

    mentor "Luar biasa! Urutan T568B kamu sempurna!"
    mc "Alhamdulillah! Lumayan juga menghafalnya..."
    show rafi malu at left with dissolve
    rafi "Anjir [nama_mc] ngerti beneran. Gue malah masih bingung urutan ke-4 sama ke-5..."
    mentor "Rafi, kabel ke-4 itu Biru, ke-5 Putih Biru. Biru dulu, baru Putih Biru."
    rafi "Ohhhh! Iya ya. Makasih Pak!"
    hide rafi with dissolve
    mentor "Oke, kita lanjut ke quest selanjutnya. Bagus [nama_mc]! +25 poin."

    jump quest3

label quest2_salah:

    scene bg lab with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    sistem "[[ CABLE TEST ]] ❌ GAGAL — Urutan pin tidak sesuai standar T568B"
    sistem "[[ HASIL ]] Salah — Terdapat urutan kabel yang tidak tepat"

    mentor "Urutan belum tepat. Ingat, salah satu pin saja bisa bikin koneksi gagal."
    mc "Waduh, harus diulang..."

    if tries_q2 >= 3:
        mentor "Sudah dicoba [tries_q2] kali. Ayo fokus — urutannya: Putih Orange, Orange, Putih Hijau, Biru, Putih Biru, Hijau, Putih Coklat, Coklat."
        mentor "Ingat caranya: mulai dari Orange, lalu Hijau, lalu Biru, lalu Coklat. Setiap warna didahului warna Putih."
    else:
        mentor "Coba lagi ya. Perhatikan urutannya dengan teliti."

    jump quest2_mulai

## ============================================================
## ─── ACT 3: TROUBLESHOOTING ─────────────────────────────────
## ============================================================

label quest3:

    scene bg kantor with dissolve
    show screen hud_score

    narasi "═══ ACT 3: TROUBLESHOOTING ═══"
    narasi "Tiba-tiba HP Pak Hendra berbunyi. Ada laporan masalah dari user."

    show mentor tegas at right
    show client panik at left with hpunch

    client "Pak Hendra! Internet di ruang saya tidak bisa konek sama sekali sejak tadi pagi!"
    client "Saya tidak bisa akses sistem ERP, meeting online juga gagal. Ini darurat!"
    mentor "Tenang Bu Dewi. [nama_mc] yang baru bergabung akan bantu troubleshoot."
    client "Hah?! Teknisi baru?! Bisa dipercaya tidak?!"
    mentor "[nama_mc], ini kesempatanmu. Tangani dengan benar."

    hide mentor with dissolve
    hide client with dissolve

    mc "Baik... saya perlu cek dulu dari mana masalahnya."

    narasi "─── GEJALA ───"
    narasi "• PC Bu Dewi tidak bisa akses internet"
    narasi "• IP Address: 192.168.1.45"
    narasi "• Subnet Mask: 255.255.255.0"
    narasi "• Default Gateway: 192.168.1.1"
    narasi "• DNS: 8.8.8.8"
    narasi "• Lampu indikator port switch MATI untuk port Bu Dewi"

    narasi "Apa langkah pertama troubleshooting yang kamu ambil?"

label quest3_pilih:

    $ tries_q3 += 1

    menu:
        "Cek kabel LAN dan Port Switch":
            jump quest3_benar

        "Langsung restart PC Bu Dewi":
            jump quest3_salah_a

        "Format ulang PC Bu Dewi":
            jump quest3_salah_b

        "Hubungi ISP dan minta ganti modem":
            jump quest3_salah_c

label quest3_benar:

    $ score += 20
    scene bg kantor with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve

    mc "Saya cek dulu kabelnya, Pak."

    sistem "[[ CEK FISIK ]] Kabel LAN pada port switch... TERLEPAS!"
    sistem "[[ ACTION ]] Re-plug kabel ke port... ✅"
    sistem "[[ PING 192.168.1.1 ]] Reply from 192.168.1.1: time=2ms ✅"
    sistem "[[ PING 8.8.8.8 ]] Reply from 8.8.8.8: time=12ms ✅"
    sistem "[[ STATUS ]] ✅ CONNECTED — Masalah terselesaikan!"

    show client neutral at left with dissolve
    client "Oh! Internet sudah menyala lagi! Terima kasih banyak!"
    mc "Sama-sama Bu Dewi. Ternyata kabelnya terlepas dari switch."
    client "Wah, hal kecil tapi bikin panik. Hehehe..."
    hide client with dissolve

    mentor "Bagus! Troubleshooting yang benar dimulai dari lapisan Physical (Layer 1 OSI Model)."
    mentor "Bottom-up approach: fisik dulu, baru software. Itu metodologi yang tepat."

    narasi "─── PENJELASAN OSI MODEL ───"
    narasi "Layer 1 (Physical): Kabel, konektor, sinyal listrik/optik"
    narasi "Layer 2 (Data Link): MAC address, switch, Ethernet frame"
    narasi "Layer 3 (Network): IP address, router, routing"
    narasi "Layer 4 (Transport): TCP/UDP, port number"
    narasi "Layer 7 (Application): HTTP, HTTPS, FTP, SSH"

    mentor "+20 poin! Tapi jangan puas dulu — tantangan lebih besar menunggu."
    jump climax

label quest3_salah_a:

    scene bg kantor with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mc "Saya restart PC-nya dulu ya Bu."
    sistem "[[ PC RESTART ]] Rebooting..."
    sistem "[[ STATUS ]] ❌ Masalah tidak terselesaikan — IP lampu switch masih MATI"
    show client panik at left with vpunch
    client "Sudah restart tapi tetap tidak bisa Pak!"
    hide client with dissolve
    mentor "Restart bukan solusi utama. Kalau lampu switch mati, masalahnya di fisik atau konektivitas."
    mentor "Mulai dari yang paling sederhana: apakah kabelnya terpasang dengan benar?"

    if tries_q3 >= 3:
        mentor "Sudah [tries_q3] kali coba. Ingat OSI Layer: mulai dari Physical Layer (kabel) dulu!"
    jump quest3_pilih

label quest3_salah_b:

    scene bg kantor with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mc "Mungkin perlu diformat ulang PC-nya..."
    show client panik at left with hpunch
    client "HAAAAH?! Format ulang?! Data saya bagaimana?!"
    hide client with dissolve
    mentor "STOP! Format ulang bukan solusi untuk masalah koneksi seperti ini."
    mentor "Itu tindakan ekstrem yang tidak perlu. Cek fisik dulu sebelum langkah apapun!"

    if tries_q3 >= 3:
        mentor "Sudah [tries_q3] kali salah. Hint: lihat lampu indikator switch — apa artinya lampu mati?"
    jump quest3_pilih

label quest3_salah_c:

    scene bg kantor with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mc "Mungkin masalahnya dari ISP, saya hubungi mereka..."
    sistem "[[ ISP SUPPORT ]] Menghubungi ISP..."
    sistem "[[ ISP ]] Koneksi dari sisi kami normal. Silahkan cek internal."
    mentor "Tentu saja! ISP tidak ada masalah — ini masalah internal kita."
    mentor "Jangan langsung blame ISP. Cek jaringan internal dulu dari ujung ke ujung."

    if tries_q3 >= 3:
        mentor "Sudah [tries_q3] kali. Clue: lampu switch MATI di port Bu Dewi. Apa yang mungkin terjadi?"
    jump quest3_pilih

## ============================================================
## ─── ACT 4: CLIMAX (NETWORK DOWN) ──────────────────────────
## ============================================================

label climax:

    play music "audio/bgm_trouble.mp3" fadein 1.0 volume 0.8
    scene bg serverroom with dissolve
    show screen hud_score

    narasi "═══ ACT 4: CLIMAX — TOTAL NETWORK FAILURE ═══"

    narasi "Alarm NMS (Network Management System) berbunyi keras."
    narasi "Semua monitor di ruang server menampilkan warning merah."

    show mentor tegas at right
    show rafi bingung at left with hpunch

    sistem "[[ ALERT ]] ❌❌❌ CRITICAL — Seluruh jaringan kantor DOWN!"
    sistem "[[ AFFECTED ]] 5 switch, 2 router, 150+ workstation tidak dapat terhubung"
    sistem "[[ PING GATEWAY ]] Request Timed Out"
    sistem "[[ DHCP ]] Server tidak merespons"

    mentor "Ini gawat darurat! Seluruh infrastruktur down. Kita harus diagnosa segera!"
    rafi "Ini... ini gimana caranya? Gue nggak pernah lihat yang separah ini..."
    mentor "[nama_mc]! Kamu yang paling fresh study. Analisa situasinya!"

    hide rafi with dissolve

    narasi "─── DATA DIAGNOSTIK ───"
    narasi "• Core Switch (pusat) tidak merespons"
    narasi "• DHCP server tidak memberikan IP"
    narasi "• Semua workstation dapat IP 169.254.x.x (APIPA)"
    narasi "• Log terakhir: 'Spanning Tree Loop Detected'"
    narasi "• Ada kabel baru dipasang kemarin oleh teknisi lain"
    narasi "• Power supply UPS normal"

    narasi "Apa analisis dan solusi yang tepat?"

label climax_pilih:

    $ tries_climax += 1

    menu:
        "Restart semua switch satu per satu":
            jump climax_salah_a

        "Broadcast storm (loop) isolasi & matikan port":
            jump climax_benar_b

        "Ganti semua kabel jaringan":
            jump climax_salah_c

        "Reset factory semua perangkat jaringan":
            jump climax_salah_d

label climax_benar:

    $ score += 30
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    show rafi malu at left with dissolve

    mc "Berdasarkan data, ini broadcast storm akibat Spanning Tree loop!"
    mc "Kabel baru yang dipasang kemarin sepertinya membuat loop di topologi."
    mc "Solusi: isolasi port yang mencurigakan dulu, aktifkan STP dengan benar!"

    sistem "[[ ACTION ]] Identifying loop port on Core Switch..."
    sistem "[[ FOUND ]] Port Fa0/24 — Gi1/0/1 loop detected"
    sistem "[[ ACTION ]] Shutdown port loop..."
    sistem "[[ STP ]] Spanning Tree Protocol re-converging..."
    sistem "[[ DHCP ]] Server online — distributing IP addresses..."
    sistem "[[ STATUS ]] ✅ ALL SYSTEMS ONLINE — Network restored!"

    mentor "BRILIAN! Analisis yang sempurna, [nama_mc]!"
    mc "Broadcast storm terjadi ketika ada loop di topologi Ethernet tanpa STP yang benar."
    mentor "Tepat sekali. STP (Spanning Tree Protocol) mencegah loop dengan memblokir port redundan."
    mentor "Kemarin ada kabel backup dipasang tanpa konfigurasi STP yang benar — itu penyebabnya."
    rafi "Wahhh... gue baru tau ada yang namanya broadcast storm. Keren banget analisisnya [nama_mc]!"
    hide rafi with dissolve
    mentor "+30 poin! Kamu benar-benar luar biasa. Saatnya evaluasi akhir."

    jump ending_check

label climax_salah_a:

    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mc "Saya restart semua switch satu per satu..."
    sistem "[[ ACTION ]] Restarting switches..."
    sistem "[[ STATUS ]] ❌ Setelah restart, broadcast storm kembali terjadi"
    sistem "[[ WARNING ]] Root cause belum diatasi!"
    mentor "Restart tanpa mengatasi root cause hanya solusi sementara."
    mentor "Data diagnostik menunjuk ke broadcast storm — fokus ke sana!"

    if tries_climax >= 3:
        mentor "Clue: IP 169.254.x.x adalah APIPA — DHCP tidak jalan. Kenapa? Karena loop membanjiri network."
    jump climax_pilih

label climax_salah_b:

    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mc "Kita ganti semua kabel jaringan!"
    mentor "Kita punya 150+ workstation. Ganti semua kabel akan butuh berhari-hari!"
    mentor "Masalahnya bukan kabel rusak, tapi topologi yang salah. Lihat log STP!"

    if tries_climax >= 3:
        mentor "Petunjuk: 'Spanning Tree Loop Detected' di log. Apa itu artinya?"
    jump climax_pilih

label climax_salah_c:

    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mc "Factory reset semua perangkat!"
    mentor "ITU AKAN MENGHAPUS SEMUA KONFIGURASI PRODUKSI!"
    mentor "VLAN, routing table, ACL — semua hilang! Kita tidak bisa melakukan itu."
    mentor "Diagnosa dulu, baru ambil tindakan yang proporsional."

    if tries_climax >= 3:
        mentor "Ingat: 'Spanning Tree Loop Detected' + kabel baru kemarin = loop di topologi!"
    jump climax_pilih

## ============================================================
## ─── ACT 5: ENDING ──────────────────────────────────────────
## ============================================================

label ending_check:

    hide screen hud_score
    scene bg kantor with dissolve

    show admin serius at right
    show mentor neutral at left with hpunch

    narasi "═══ ACT 5: EVALUASI AKHIR ═══"
    narasi "Hari terakhir magang. Pak Admin IT dipanggil untuk evaluasi kinerja."

    $ grade = get_grade()

    admin "Pak Hendra, bagaimana performa [nama_mc] selama magang?"
    mentor "Cukup memuaskan, Pak. Terutama saat debugging jaringan tadi."
    admin "[nama_mc], saya sudah lihat semua laporan kerjamu. Skor akhir kamu: [score] poin. Grade: [grade]."

    pause 1.0

    $ ending = get_ending_type()

    if ending == "pro":
        jump ending_pro
    elif ending == "mid":
        jump ending_mid
    else:
        jump ending_bad

## ─── ENDING 1: TEKNISI PRO ──────────────────────────────────

label ending_pro:

    play music "audio/bgm_success.mp3" fadein 1.0
    scene bg ending_ok with dissolve

    show admin happy at right, loncat
    show mentor senyum at left with dissolve

    narasi "✦ ENDING 1: TEKNISI PROFESIONAL ✦"

    admin "[nama_mc], hasil evaluasimu sangat memuaskan! Skor [score] poin — Grade [grade]."
    admin "Kamu berhasil menangani semua kasus dengan metodologi yang tepat."
    admin "Kami memutuskan... untuk merekrutmu sebagai teknisi tetap di PT. Nusanet Teknologi!"

    mc "Sungguh?! Terima kasih banyak, Pak!"

    show mentor senyum at left
    mentor "Saya tidak kecewa melatihmu, [nama_mc]. Kamu memang berbakat."
    mentor "Tapi ingat — di dunia IT, berhenti belajar berarti tertinggal."
    mc "Siap Pak! Saya akan terus belajar. Terima kasih sudah membimbing saya."

    show rafi malu at center with dissolve
    rafi "Selamat [nama_mc]!! Nanti kalau gue juga lulus, ajari gue ya hahaha!"
    mc "Hahaha, siap Rafi! Kita belajar bareng!"
    hide rafi with dissolve

    narasi "♦ REKAP AKHIR ♦"
    narasi "Skor Total: [score] poin | Grade: [grade]"
    narasi "Status: ✅ DIREKRUT sebagai Teknisi Tetap"
    narasi ""
    narasi "Konsep yang dikuasai:"
    narasi "  ✓ Jenis kabel UTP (Straight-through vs Crossover)"
    narasi "  ✓ Standar crimping T568B"
    narasi "  ✓ Troubleshooting dengan OSI Layer (bottom-up)"
    narasi "  ✓ Analisis broadcast storm & Spanning Tree Protocol"
    narasi ""
    narasi "   「 Selamat! Kamu adalah Teknisi Jaringan Sejati! 」"

    jump game_over

## ─── ENDING 2: PERLU BELAJAR LAGI ──────────────────────────

label ending_mid:

    stop music fadeout 2.0
    scene bg ending_mid with dissolve

    show admin neutral at right with dissolve
    show mentor neutral at left with dissolve

    narasi "✦ ENDING 2: TEKNISI DALAM PENGEMBANGAN ✦"

    admin "[nama_mc], hasil evaluasimu cukup baik. Skor [score] poin — Grade [grade]."
    admin "Kamu menunjukkan potensi, tapi masih ada beberapa area yang perlu ditingkatkan."
    admin "Kami menawarkan perpanjangan masa magang selama 3 bulan."
    admin "Gunakan kesempatan ini untuk memperdalam skill jaringanmu."

    mc "Baik, Pak. Saya terima. Saya masih perlu banyak belajar."

    show mentor tegas at left
    mentor "Jangan kecewa [nama_mc]. Ini bukan kegagalan, ini kesempatan."
    mentor "Ulangi materi dasar: OSI Model, subnetting, dan protokol routing."
    mc "Siap Pak Hendra. Saya tidak akan menyia-nyiakan kesempatan ini!"

    narasi "♦ REKAP AKHIR ♦"
    narasi "Skor Total: [score] poin | Grade: [grade]"
    narasi "Status: 🔄 PERPANJANGAN MAGANG (3 bulan)"
    narasi ""
    narasi "Area yang perlu diperbaiki:"
    narasi "  → Kecepatan identifikasi masalah jaringan"
    narasi "  → Pemahaman protokol layer 2 & 3"
    narasi "  → Systematic troubleshooting methodology"
    narasi ""
    narasi "   「 Terus semangat! Ilmu tidak ada habisnya. 」"

    jump game_over

## ─── ENDING 3: GAGAL ────────────────────────────────────────

label ending_bad:

    stop music fadeout 2.0
    scene bg ending_bad with dissolve

    show admin serius at right with dissolve
    show mentor tegas at left with dissolve

    narasi "✦ ENDING 3: PERLU PERSIAPAN LEBIH ✦"

    admin "[nama_mc], saya harus jujur. Skor [score] poin — Grade [grade]."
    admin "Sayangnya, kami tidak bisa melanjutkan masa magangmu saat ini."
    admin "Namun ini bukan akhir dari segalanya."

    mc "Saya... mengerti, Pak. Maaf telah mengecewakan."

    show mentor neutral at left
    mentor "Jangan berkecil hati [nama_mc]. Setiap teknisi handal pernah berada di posisimu."
    mentor "Kembali ke sekolah, perkuat dasarnya, dan coba lagi."
    mentor "Rekomendasi saya: pelajari CCNA, ikuti praktikum jaringan lebih intensif."
    mc "Terima kasih sudah membimbing saya, Pak Hendra. Saya akan kembali lebih siap!"

    narasi "♦ REKAP AKHIR ♦"
    narasi "Skor Total: [score] poin | Grade: [grade]"
    narasi "Status: ❌ Magang Tidak Dilanjutkan"
    narasi ""
    narasi "Rekomendasi pembelajaran:"
    narasi "  📚 Pelajari OSI Model 7 Layer secara mendalam"
    narasi "  📚 Latihan crimping kabel UTP sampai hafal di luar kepala"
    narasi "  📚 Ikuti simulasi Cisco Packet Tracer"
    narasi "  📚 Pelajari subnetting IPv4 & IPv6"
    narasi ""
    narasi "   「 Kegagalan adalah guru terbaik. Bangkit dan coba lagi! 」"

    jump game_over

## ─── CHAPTER 1 COMPLETE ─────────────────────────────────────

label game_over:

    play music "audio/bgm_success.mp3" fadein 1.5
    scene bg luar with fade
    pause 0.5

    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "          ★  CHAPTER 1 SELESAI  ★"
    narasi "    NetPro: Magang Jaringan — TKJ Edition"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    narasi "📋 Rekap Perjalanan [nama_mc] di Chapter 1:"
    narasi "  🔌 Quest 1 — Jenis Kabel UTP (Straight-through vs Crossover)"
    narasi "  🛠️  Quest 2 — Crimping Kabel T568B"
    narasi "  🔍 Quest 3 — Troubleshooting Jaringan (OSI Bottom-Up)"
    narasi "  ⚡ Climax  — Broadcast Storm & Spanning Tree Protocol"
    narasi ""
    narasi "🏆 Skor Akhir Chapter 1: [score] poin | Grade: [grade]"
    narasi ""
    narasi "Sebelum melanjutkan ke Chapter 2..."
    narasi "Mari kita pastikan kamu benar-benar menguasai materi Chapter 1!"

    menu:
        "Lanjut ke Kuis Refleksi Chapter 1 →":
            jump refleksi_quiz

        "Ulangi Chapter 1 dari awal":
            jump start

## ============================================================
## ─── REFLEKSI KUIS CHAPTER 1 ────────────────────────────────
## ============================================================

label refleksi_quiz:

    stop music fadeout 1.5
    play music "audio/bgm_main.mp3" fadein 1.5
    scene bg lab with dissolve
    $ refleksi_score = 0

    narasi ""
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"
    narasi "      REFLEKSI MATERI — CHAPTER 1"
    narasi "   Jawab 5 pertanyaan berikut dengan cermat!"
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"
    narasi ""

    show mentor senyum at right with dissolve
    mentor "Oke [nama_mc], saatnya kita review materi Chapter 1 sebelum lanjut!"
    mentor "Ada 5 soal — jawab dengan percaya diri. Setiap jawaban benar = +10 poin bonus!"
    hide mentor with dissolve

    ## ═══════ SOAL 1 ═══════
    narasi "── SOAL 1 ──────────────────────────────────────"
    narasi "🔌 Kabel jenis apa yang digunakan untuk menghubungkan PC ke Switch?"
    narasi ""

    menu:
        "A. Crossover":
            show mentor tegas at right with dissolve
            mentor "❌ Salah! Crossover digunakan untuk menghubungkan perangkat SEJENIS (PC ke PC, Switch ke Switch)."
            mentor "Untuk PC ke Switch (perangkat berbeda), gunakan kabel Straight-through."
            hide mentor with dissolve

        "B. Straight-through ✓":
            $ refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Benar! Straight-through digunakan antara perangkat yang BERBEDA jenis seperti PC ke Switch."
            hide mentor with dissolve

        "C. Fiber Optic":
            show mentor tegas at right with dissolve
            mentor "❌ Belum tepat. Fiber Optic adalah media transmisi, bukan tipe kabel berdasarkan susunan pin."
            mentor "Untuk PC ke Switch, jawabannya adalah Straight-through."
            hide mentor with dissolve

        "D. Rollover":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. Rollover/Console dipakai untuk koneksi ke port console router/switch, bukan untuk data."
            mentor "Untuk PC ke Switch, gunakan kabel Straight-through!"
            hide mentor with dissolve

    ## ═══════ SOAL 2 ═══════
    narasi "── SOAL 2 ──────────────────────────────────────"
    narasi "🎨 Pada standar T568B, kabel pada pin ke-1 berwarna apa?"
    narasi ""

    menu:
        "A. Orange":
            show mentor tegas at right with dissolve
            mentor "❌ Hampir! Orange ada di pin ke-2. Pin ke-1 adalah PUTIH Orange (campuran putih & orange)."
            hide mentor with dissolve

        "B. Putih Hijau":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. Putih Hijau ada di pin ke-3. Ingat urutan: Putih Orange, Orange, Putih Hijau..."
            hide mentor with dissolve

        "C. Putih Orange ✓":
            $ refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Tepat! Pin 1 = Putih Orange. Urutan lengkap: PO-O-PH-B-PB-H-PC-C"
            hide mentor with dissolve

        "D. Biru":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. Biru ada di pin ke-4. Pin ke-1 adalah Putih Orange!"
            hide mentor with dissolve

    ## ═══════ SOAL 3 ═══════
    narasi "── SOAL 3 ──────────────────────────────────────"
    narasi "🗂️  Dalam OSI Model, Physical Layer berada di layer ke berapa?"
    narasi ""

    menu:
        "A. Layer 3":
            show mentor tegas at right with dissolve
            mentor "❌ Layer 3 adalah Network Layer (IP Address, Router). Physical Layer ada di Layer 1!"
            hide mentor with dissolve

        "B. Layer 2":
            show mentor tegas at right with dissolve
            mentor "❌ Layer 2 adalah Data Link Layer (MAC Address, Switch). Physical Layer ada di Layer 1!"
            hide mentor with dissolve

        "C. Layer 7":
            show mentor tegas at right with dissolve
            mentor "❌ Layer 7 adalah Application Layer (HTTP, DNS). Physical Layer = Layer 1 (paling bawah)!"
            hide mentor with dissolve

        "D. Layer 1 ✓":
            $ refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Benar! Physical Layer = Layer 1. Kabel, konektor, dan sinyal listrik ada di sini."
            mentor "Troubleshooting bottom-up artinya mulai dari Layer 1 ini!"
            hide mentor with dissolve

    ## ═══════ SOAL 4 ═══════
    narasi "── SOAL 4 ──────────────────────────────────────"
    narasi "🌐 IP Address 169.254.x.x pada workstation menandakan kondisi apa?"
    narasi ""

    menu:
        "A. IP publik yang diberikan ISP":
            show mentor tegas at right with dissolve
            mentor "❌ IP publik biasanya range seperti 103.x.x.x atau 202.x.x.x — bukan 169.254."
            mentor "169.254.x.x adalah APIPA — tanda DHCP server tidak menjawab!"
            hide mentor with dissolve

        "B. DHCP server tidak memberikan IP (APIPA) ✓":
            $ refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Tepat! APIPA = Automatic Private IP Addressing. Windows otomatis assign 169.254.x.x"
            mentor "jika DHCP server tidak bisa dihubungi. Ini tanda ada masalah di jaringan!"
            hide mentor with dissolve

        "C. Tanda koneksi internet sangat cepat":
            show mentor tegas at right with dissolve
            mentor "❌ Justru sebaliknya! 169.254.x.x berarti tidak ada koneksi — DHCP gagal menjawab."
            hide mentor with dissolve

        "D. Koneksi ke server berhasil":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. 169.254.x.x (APIPA) berarti DHCP server tidak bisa dihubungi sama sekali!"
            hide mentor with dissolve

    ## ═══════ SOAL 5 ═══════
    narasi "── SOAL 5 ──────────────────────────────────────"
    narasi "🔄 Fungsi utama STP (Spanning Tree Protocol) dalam jaringan Ethernet adalah?"
    narasi ""

    menu:
        "A. Mengatur kecepatan unduh/unggah internet":
            show mentor tegas at right with dissolve
            mentor "❌ Itu bukan fungsi STP. Kecepatan diatur oleh QoS atau bandwidth management."
            mentor "STP bertugas mencegah loop di jaringan Ethernet!"
            hide mentor with dissolve

        "B. Mengamankan password WiFi":
            show mentor tegas at right with dissolve
            mentor "❌ Keamanan WiFi ditangani oleh WPA/WPA2/WPA3, bukan STP."
            mentor "STP = Spanning Tree Protocol, pencegah loop di switch!"
            hide mentor with dissolve

        "C. Mencegah network loop pada topologi Ethernet ✓":
            $ refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ BENAR! STP memblokir port redundan untuk mencegah broadcast storm."
            mentor "Inilah yang menyelamatkan jaringan tadi dari Spanning Tree Loop!"
            hide mentor with dissolve

        "D. Memberikan IP address otomatis ke perangkat":
            show mentor tegas at right with dissolve
            mentor "❌ IP address otomatis diberikan oleh DHCP, bukan STP."
            mentor "STP = Spanning Tree Protocol, fungsinya mencegah loop!"
            hide mentor with dissolve

    ## ═══════ HASIL REFLEKSI ═══════
    scene bg kantor with dissolve

    show mentor neutral at right with dissolve
    show rafi neutral at left with dissolve

    narasi ""
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    narasi "      HASIL REFLEKSI CHAPTER 1"
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    narasi ""
    narasi "Skor Refleksi: [refleksi_score] / 50 poin"

    if refleksi_score == 50:
        $ score += 20
        narasi "Nilai: ⭐⭐⭐ SEMPURNA! +20 bonus poin!"
        mentor "Luar biasa! Semua soal benar! Kamu benar-benar menguasai materi Chapter 1!"
        mentor "Kamu dapat 20 poin bonus! Total skor kamu sekarang: [score] poin!"
        rafi "Gila [nama_mc]! Semua bener?! Ajakkin gue belajar bareng dong 😭"
    elif refleksi_score >= 30:
        $ score += 10
        narasi "Nilai: ⭐⭐ BAIK! +10 bonus poin!"
        mentor "Bagus! Kamu sudah cukup menguasai dasar-dasar Chapter 1."
        mentor "+10 poin bonus! Tapi pastikan kamu review soal yang salah sebelum Chapter 2!"
        rafi "Lumayan [nama_mc]! Ayo terus semangat!"
    else:
        narasi "Nilai: ⭐ PERLU BELAJAR LAGI"
        mentor "Hmm, masih ada beberapa konsep yang perlu diulang."
        mentor "Tidak apa-apa — di Chapter 2, kamu akan semakin paham."
        mentor "Yang penting: Straight-through = beda perangkat, Crossover = sama perangkat. Ingat ya!"
        rafi "Jangan menyerah [nama_mc]! Kita belajar bareng yuk 💪"

    hide rafi with dissolve

    narasi ""
    narasi "━━━━━ RINGKASAN MATERI CHAPTER 1 ━━━━━"
    narasi "✅ Kabel UTP: Straight-through (beda perangkat) | Crossover (sama perangkat)"
    narasi "✅ T568B: PO-O-PH-B-PB-H-PC-C (8 pin berurutan)"
    narasi "✅ OSI Layer 1 = Physical | Layer 2 = Data Link | Layer 3 = Network"
    narasi "✅ APIPA 169.254.x.x = DHCP server tidak menjawab"
    narasi "✅ STP = Spanning Tree Protocol (mencegah broadcast storm/loop)"
    narasi ""

    mentor "Sip! Sekarang kamu siap untuk tantangan berikutnya."
    mentor "Chapter 2 akan jauh lebih menantang — tentang VLAN dan segmentasi jaringan!"

    menu:
        "Lanjut ke Chapter 2! →":
            jump chapter2

        "Ulangi kuis refleksi":
            jump refleksi_quiz

        "Kembali ke Menu Utama":
            return

## ============================================================
## ─── CHAPTER 2: VLAN & SEGMENTASI JARINGAN ──────────────────
## ============================================================

label chapter2:

    play music "audio/bgm_main.mp3" fadein 1.5
    scene bg kantor with fade
    $ ch2_score = 0
    $ tries_ch2_q1 = 0
    $ tries_ch2_q2 = 0
    $ tries_ch2_q3 = 0
    $ tries_ch2_climax = 0

    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "       ⚡  CHAPTER 2 DIMULAI  ⚡"
    narasi "   VLAN & Segmentasi Jaringan Kantor"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    narasi "Minggu ke-2 magang di PT. Nusanet Teknologi."
    narasi "[nama_mc] sudah lebih percaya diri setelah berhasil di Chapter 1."
    narasi "Namun tantangan yang lebih besar sudah menunggu..."

    show mentor neutral at right with dissolve
    mentor "[nama_mc], ada kabar besar. Perusahaan akan menambah 2 divisi baru: Marketing dan Finance."
    mentor "Jaringan kita saat ini masih flat — semua perangkat di satu network yang sama."
    mentor "Ini berbahaya! Finance tidak boleh bisa langsung akses server Marketing, dan sebaliknya."
    mc "Saya mengerti, Pak. Kita perlu segmentasi jaringan?"
    show mentor senyum at right
    mentor "Tepat! Kita akan menggunakan VLAN — Virtual Local Area Network."
    mentor "Siapkan dirimu, [nama_mc]. Chapter 2 dimulai sekarang!"
    hide mentor with dissolve

    jump ch2_quest1

## ============================================================
## ─── CH2 QUEST 1: SUBNETTING ─────────────────────────────────
## ============================================================

label ch2_quest1:

    scene bg lab with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH2 QUEST 1: SUBNETTING IP ADDRESS ═══"

    mentor "Kita punya satu blok IP: 192.168.10.0/24"
    mentor "Harus dibagi untuk 3 divisi: IT, Marketing, dan Finance."
    mentor "Masing-masing butuh maksimal 50 host. Subnet mask yang tepat adalah /26."

    show rafi bingung at left with dissolve
    rafi "Hmm... /24 itu 254 host kan? Kenapa harus disubnet lagi?"
    mentor "Karena kalau semua dalam satu network, semua bisa 'dengar' broadcast satu sama lain."
    mentor "Ini boros bandwidth dan tidak aman. /26 memberi 62 host per subnet — cukup untuk tiap divisi."
    rafi "Ohh jadi lebih efisien dan aman. Ngerti deh!"
    hide rafi with dissolve

    narasi "─── DATA SUBNETTING ───"
    narasi "• Network asal : 192.168.10.0/24"
    narasi "• Subnet mask /26 = 255.255.255.192"
    narasi "• Tiap subnet  : 64 alamat (62 host + network + broadcast)"
    narasi ""
    narasi "Pertanyaan: Subnet ke-2 berada di range IP berapa?"

label ch2_q1_pilih:

    $ tries_ch2_q1 += 1

    menu:
        "192.168.10.64 — 192.168.10.127":
            jump ch2_q1_benar

        "192.168.10.0 — 192.168.10.63":
            jump ch2_q1_salah_a

        "192.168.10.128 — 192.168.10.191":
            jump ch2_q1_salah_b

        "192.168.10.100 — 192.168.10.163":
            jump ch2_q1_salah_c

label ch2_q1_benar:

    $ ch2_score += 20
    scene bg lab with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve

    sistem "[[ SUBNET CALC ]] ✅ Tepat!"
    sistem "[[ Subnet 1 ]] 192.168.10.0   — 192.168.10.63   → IT Dept"
    sistem "[[ Subnet 2 ]] 192.168.10.64  — 192.168.10.127  → Marketing"
    sistem "[[ Subnet 3 ]] 192.168.10.128 — 192.168.10.191  → Finance"

    mc "Subnet ke-2 dimulai dari .64 karena setiap blok /26 berisi 64 alamat!"
    mentor "Benar sekali! .0-.63 = IT, .64-.127 = Marketing, .128-.191 = Finance."
    mentor "Network address .64, broadcast .127, host valid .65 sampai .126."
    mentor "+20 poin! Sekarang kita bisa mulai konfigurasi VLAN di switch."

    jump ch2_quest2

label ch2_q1_salah_a:

    scene bg lab with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mentor "Itu subnet ke-1 (192.168.10.0/26) — yang dipakai divisi IT."
    mentor "Subnet ke-2 dimulai dari angka SETELAH broadcast subnet pertama (.63)."
    if tries_ch2_q1 >= 3:
        mentor "Hint: Setiap /26 punya 64 alamat. Subnet 1 = 0..63. Subnet 2 mulai dari 0+64 = .64"
    jump ch2_q1_pilih

label ch2_q1_salah_b:

    scene bg lab with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mentor "Itu subnet ke-3 (192.168.10.128/26) — untuk divisi Finance."
    mentor "Kita perlu subnet ke-2. Ingat, setiap blok /26 berisi 64 alamat."
    if tries_ch2_q1 >= 3:
        mentor "Hint: Subnet 1 = .0-.63, Subnet 2 = .64-.127, Subnet 3 = .128-.191"
    jump ch2_q1_pilih

label ch2_q1_salah_c:

    scene bg lab with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve

    mentor "192.168.10.100-.163 bukan range subnet yang valid untuk /26."
    mentor "Subnet harus mulai dari kelipatan 64: .0, .64, .128, .192."
    if tries_ch2_q1 >= 3:
        mentor "Hint: /26 = blok 64 alamat. Subnet ke-2 dimulai dari 192.168.10.64!"
    jump ch2_q1_pilih


## ============================================================
## ─── CH2 QUEST 2: KONFIGURASI VLAN ──────────────────────────
## ============================================================

label ch2_quest2:

    scene bg serverroom with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH2 QUEST 2: KONFIGURASI VLAN DI SWITCH ═══"

    mentor "Sekarang IP sudah dibagi. Waktunya mengkonfigurasi switch dengan VLAN."
    mentor "VLAN 10 untuk IT, VLAN 20 untuk Marketing, VLAN 30 untuk Finance."

    show client panik at left with dissolve
    client "Pak Hendra! Saya Bu Dewi dari Finance. Saya cek di Network, kok saya bisa buka folder rahasia Marketing?!"
    mentor "Tenang Bu. Karena belum pakai VLAN, switch masih bertindak sebagai 1 broadcast domain."
    mentor "Sekarang [nama_mc] akan mengelompokkan port-port di switch."
    hide client with dissolve

    narasi "─── KEBUTUHAN PORT ───"
    narasi "• Port Fa0/1 - Fa0/10   : IT Dept (VLAN 10)"
    narasi "• Port Fa0/11 - Fa0/20  : Marketing (VLAN 20)"
    narasi "• Port Fa0/21 - Fa0/24  : Finance (VLAN 30)"
    narasi ""
    narasi "Pertanyaan: Perintah Cisco IOS apa yang digunakan untuk mengatur port masuk ke VLAN tertentu?"

label ch2_q2_pilih:

    $ tries_ch2_q2 += 1

    menu:
        "switchport mode trunk":
            jump ch2_q2_salah_a

        "switchport access vlan <ID>":
            jump ch2_q2_benar

        "vlan database <ID>":
            jump ch2_q2_salah_b

        "ip address 192.168.10.<ID>":
            jump ch2_q2_salah_c

label ch2_q2_benar:

    $ ch2_score += 20
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve

    sistem "[[ SWITCH CONFIG ]] Switch(config-if)# switchport access vlan 20"
    sistem "[[ LOG ]] Interface Fa0/11 changed state to up, assigned to VLAN 20"
    sistem "[[ SECURE ]] Finance tidak lagi bisa mengakses folder Marketing (Beda VLAN)."

    mc "Kita gunakan 'switchport access vlan <ID>' untuk mengatur port menjadi access mode ke VLAN spesifik!"
    mentor "Tepat sekali. Port ke komputer klien disebut 'Access Port' karena hanya membawa traffic 1 VLAN saja."
    mentor "Sekarang traffic Marketing dan Finance sudah terisolasi di level Layer 2. +20 Poin!"
    
    jump ch2_quest3

label ch2_q2_salah_a:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Salah. 'Trunk' digunakan untuk port yang terhubung ke switch lain atau router, membawa banyak VLAN sekaligus."
    mentor "Untuk PC Klien (End device), kita gunakan port type 'Access'."
    if tries_ch2_q2 >= 3:
        mentor "Hint: Gunakan perintah untuk mengatur 'access' vlan."
    jump ch2_q2_pilih

label ch2_q2_salah_b:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Perintah 'vlan database' (sekarang obsolete) bisa dipakai buat mendaftarkan VLAN, tapi bukan untuk masukin port ke VLAN itu."
    if tries_ch2_q2 >= 3:
        mentor "Hint: Gunakan 'switchport'..."
    jump ch2_q2_pilih

label ch2_q2_salah_c:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Itu perintah memberikan IP, bukan memasukkan port fisik (interface) ke VLAN."
    mentor "Kita butuh sintaks untuk mengubah setting switchport."
    if tries_ch2_q2 >= 3:
        mentor "Hint: Gunakan perintah switchport access."
    jump ch2_q2_pilih


## ============================================================
## ─── CH2 QUEST 3: INTER-VLAN ROUTING ────────────────────────
## ============================================================

label ch2_quest3:
    scene bg kantor with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH2 QUEST 3: INTER-VLAN ROUTING ═══"

    show rafi bingung at left with dissolve
    rafi "Pak Hendra, VLAN-nya udah jalan. Finance aman, Marketing aman."
    rafi "TAPI... Marketing ngeluh nggak bisa print dokumen ke Printer yang ada di ruangan IT (VLAN 10)!"
    mentor "Tentu saja. Perangkat di VLAN beda sama saja berada di network fisik yang beda. Layer 2 tidak menyeberang antar VLAN."
    mentor "[nama_mc], bagaimana cara agar VLAN 20 bisa mangirim data (seperti nge-print) ke VLAN 10?"

label ch2_q3_pilih:
    $ tries_ch2_q3 += 1
    
    menu:
        "Tarik lagi satu kabel sakti panjang langsung dari printer ke switch Marketing.":
            jump ch2_q3_salah_a
        "Gabungkan lagi VLAN mereka agar bisa berkomunikasi.":
            jump ch2_q3_salah_b
        "Gunakan perangkat Layer 3 (Router atau Switch L3) untuk merutekan traffic antar VLAN.":
            jump ch2_q3_benar
        "Hubungi Teknisi Printer untuk mereset driver.":
            jump ch2_q3_salah_c
            
label ch2_q3_benar:
    $ ch2_score += 25
    scene bg lab with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    sistem "[[ ROUTER CONFIG ]] Router(config)# int g0/0.20"
    sistem "[[ ROUTER CONFIG ]] Router(config-subif)# encapsulation dot1Q 20"
    sistem "[[ PING ]] Ping dari Marketing (VLAN 20) ke Printer IT (VLAN 10).... SUKSES!"

    mc "Kita bisa gunakan pendekatan Router-on-a-Stick. Satu port router diset trunk, membuat virtual sub-interface untuk tiap VLAN yang me-routing mereka secara Layer 3."
    mentor "Jenius! Betul, komunikasi 'Inter-VLAN' butuh proses routing (Layer 3)."
    mentor "Dengan ini, keamanan tetap terjaga, tapi kita bisa pakai ACL (Access Control List) untuk cuma ngizinin traffic PRINT lewat antar VLAN 20 dan 10."
    rafi "Wooow... jadi fungsi pemisahan subnet tadi ada gunanya di sini! Keren banget!"
    hide rafi with dissolve
    mentor "Kerja bagus. +25 poin."
    
    jump ch2_climax

label ch2_q3_salah_a:
    scene bg kantor with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Cara primitif. Kalau divisinya ada 10, kamu pasang 10 kartu jaringan di printernya?"
    mentor "Ada cara logikal yang lebih efisien secara network (software layer)."
    jump ch2_q3_pilih
    
label ch2_q3_salah_b:
    scene bg kantor with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Kalau digabung lagi, untuk apa cape-cape kita bikin VLAN tadi?"
    mentor "Tujuan keamanannya jebol dong. Harus tetap terpisah, tapi 'dijembatani'."
    jump ch2_q3_pilih

label ch2_q3_salah_c:
    scene bg kantor with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Teknisi printer akan nyalain ping, lihat Request timeout, dan bakal nyalahin kita (Orang Jaringan)."
    mentor "Ini murni batas Layer 2 yang tidak bisa nyebrang. Pikirkan solusi pakai perangkat jaringan Layer 3."
    jump ch2_q3_pilih

## ============================================================
## ─── CH2 CLIMAX: PORT SECURITY & INSIDEN KEAMANAN ──────────
## ============================================================

label ch2_climax:
    play music "audio/bgm_trouble.mp3" fadein 1.0 volume 0.8
    scene bg serverroom with dissolve
    show screen hud_score
    
    narasi "═══ CH2 CLIMAX: ANCAMAN PENYUSUP ═══"
    
    show mentor tegas at right
    show rafi bingung at left with hpunch
    
    rafi "Pak!! Ada tamu tak dikenal di lobi bawa laptop."
    rafi "Dia nyabut kabel LAN dari PC resepsionis, terus dia colok ke laptopnya..."
    sistem "[[ ALERT ]] UNKNOWN MAC ADDRESS DETECTED ON PORT Fa0/6"
    sistem "[[ ALERT ]] ROGUE DHCP SERVER BROADCASTS DETECTED"
    
    mentor "Gawat! Orang itu sedang berusaha menjadi 'Man in The Middle' di VLAN internal kita, atau menyebar IP palsu!"
    mentor "[nama_mc], bagaimana fitur perlindungan switch (Switchport Security) menangani kasus penyusupan fisik pada port yang sudah dikunci MAC-nya?"
    
label ch2_climax_pilih:
    $ tries_ch2_climax += 1
    
    menu:
        "Membiarkan port menyala, tapi catat peringatan (Restrict mode).":
            jump ch2_climax_salah_a
        "Otomatis memblokir IP tamu dengan Anti-Virus.":
            jump ch2_climax_salah_b
        "Menjatuhkan state port jadi err-disable / Shutdown otomatis. (Violation Shutdown)":
            jump ch2_climax_benar
        "Berlari ke lobi dan merampas laptopnya!":
            jump ch2_climax_salah_c
            
label ch2_climax_benar:
    $ ch2_score += 35
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    show rafi neutral at left with dissolve
    
    mc "Konfigurasi Switchport Port-Security dengan Violation Shutdown!"
    mc "Switch akan mendeteksi MAC asing, dan LANGSUNG mematikan port (err-disable) saat MAC tersebut mencoba transmisi!"
    
    sistem "[[ ACTION ]] Switch(config-if)# switchport port-security violation shutdown"
    sistem "[[ LOG ]] %%PM-4-ERR_DISABLE: psecure-violation error detected on Fa0/6"
    sistem "[[ LOG ]] Port Fa0/6 forced to Down state."
    sistem "[[ SAFE ]] ANCAMAN TERBLOCK DARI JARINGAN!"
    
    rafi "Wah! Lampu port di lobi langsung mati dari pusat! Keren!"
    mentor "Tepat sekali, itu pencegahan keamanan Lapis Pertama (Layer 2). +35 poin untukmu [nama_mc]!"
    mentor "Menangani insiden secepat ini mencegah data perusahaan bobol."
    hide rafi with dissolve
    
    jump ch2_ending

label ch2_climax_salah_a:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "'Restrict' memang meng-drop packet, tapi port-nya tidak dimatikan. Kalau serangan terus menerus, log kita bisa flood."
    mentor "Paling aman saat port dicuri akses fisiknya adalah mematikannya (shutdown) seketika."
    jump ch2_climax_pilih

label ch2_climax_salah_b:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Anti-virus berada di dalam OS. Ini serangan di level Switch/Kabel LAN langsung!"
    mentor "Solusinya harus dari Switch Management Layer 2."
    jump ch2_climax_pilih

label ch2_climax_salah_c:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor tegas at right with dissolve
    mentor "Walau insting yang bagus, lobi terlalu jauh buat lari, sementara serangan hitungannya mili-detik."
    mentor "Kendalikan switch-nya secara remote dan matikan port dia dari sini!"
    if tries_ch2_climax >= 2:
        mentor "Gunakan kontrol switchport dengan Violation Action tertinggi."
    jump ch2_climax_pilih


## ============================================================
## ─── CH2 ENDING ─────────────────────────────────────────────
## ============================================================

label ch2_ending:
    hide screen hud_score
    scene bg kantor with dissolve
    play music "audio/bgm_success.mp3" fadein 1.5
    
    show admin serius at right
    show mentor senyum at left with dissolve
    
    narasi "═══ CH2 EVALUASI ═══"
    
    admin "Luar biasa. Pak Hendra cerita kamu menyelamatkan dari serangan sniffing di lobi hari ini, dan merancang VLAN perusahaan."
    mentor "Total skor [nama_mc] di Chapter 2 ini luar biasa: [ch2_score] poin."
    
    if ch2_score >= 80:
        admin "Kinerja Level Enterprise! Saya akan meminta kamu memimpin deployment jaringan kantor cabang depan."
        mc "Terima kasih Pak!!"
    elif ch2_score >= 50:
        admin "Kamu paham teorinya, namun butuh belajar mengkonfigurasi dengan lebih lancar."
        mentor "Pusatkan latihan lab Cisco Packet Tracer mingguan dari sekarang."
    else:
        admin "Sepertinya Konsep Layer 2 Lanjutan (VLAN & Port Sec) belum terlalu solid dikuasai."
        mentor "Mari perbaiki literatur teori Switching basic-mu di lab sebelum praktek lapangan."

    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "          ★  CHAPTER 2 SELESAI  ★"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    narasi "🎓 Rekap Pembelajaran Chapter 2:"
    narasi "   ✓ Subnetting IPv4 CIDR (/26)"
    narasi "   ✓ Konfigurasi Access & Trunk Port (VLAN)"
    narasi "   ✓ ROAS (Router on a Stick) Inter-VLAN Routing"
    narasi "   ✓ Konsep keamanan Layer 2 (Port Security violation)"
    narasi "Sebelum melanjutkan ke tugas di Chapter 3..."
    narasi "Mari pastikan pemahaman jaringan Lapis 2-mu sudah matang!"
    
    menu:
        "Lanjut ke Kuis Refleksi Chapter 2 →":
            jump refleksi_quiz_ch2
            
        "Ulangi Chapter 2 dari awal":
            jump chapter2

## ============================================================
## ─── REFLEKSI KUIS CHAPTER 2 ────────────────────────────────
## ============================================================

label refleksi_quiz_ch2:
    stop music fadeout 1.5
    play music "audio/bgm_main.mp3" fadein 1.5
    scene bg lab with dissolve
    $ ch2_refleksi_score = 0

    narasi ""
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"
    narasi "      REFLEKSI MATERI — CHAPTER 2"
    narasi "   Jawab 5 pertanyaan berikut dengan cermat!"
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"
    narasi ""

    show mentor senyum at right with dissolve
    mentor "Siap ujimu di materi Switching dan VLAN? Setiap jawaban benar bernilai 10 poin bonus!"
    hide mentor with dissolve

    ## SOAL 1
    narasi "── SOAL 1 ──────────────────────────────────────"
    narasi "Pada Subnetting /26, berapakah jumlah IP valid (Hosts) maksimal yang bisa terhubung per subnet?"
    menu:
        "A. 128":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. /26 membagi blok menjadi 64 alamat. Jadi host validnya bukan 128."
            hide mentor with dissolve
        "B. 62 ✓":
            $ ch2_refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Benar! /26 memiliki 64 IP. Dikurangi 1 Network & 1 Broadcast = 62 IP Host valid."
            hide mentor with dissolve
        "C. 64":
            show mentor tegas at right with dissolve
            mentor "❌ Hampir! 64 adalah jumlah total IP. Namun IP pertama (Network) dan akhir (Broadcast) tidak bisa dipakai di PC."
            hide mentor with dissolve
        "D. 254":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. 254 adalah host untuk subnet /24."
            hide mentor with dissolve

    ## SOAL 2
    narasi "── SOAL 2 ──────────────────────────────────────"
    narasi "Perintah apakah yang digunakan pada konfigurasi switch untuk menjadikan port pembaca VLAN khusus ke satu PC klien?"
    menu:
        "A. switchport mode trunk":
            show mentor tegas at right with dissolve
            mentor "❌ Trunk digunakan untuk menyambung switch ke switch lain atau router."
            hide mentor with dissolve
        "B. ip address":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. Itu command Layer 3 untuk memberikan alamat ke port/vlan interfaces."
            hide mentor with dissolve
        "C. switchport mode access ✓":
            $ ch2_refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Benar! Perintah 'switchport mode access' memastikan port hanya bisa membaca VLAN tertentu."
            hide mentor with dissolve
        "D. access vlan trunk":
            show mentor tegas at right with dissolve
            mentor "❌ Tidak ada perintah sistem operasi semacam itu."
            hide mentor with dissolve

    ## SOAL 3
    narasi "── SOAL 3 ──────────────────────────────────────"
    narasi "Jika komputer di VLAN 10 ingin menge-Ping komputer di VLAN 20. Apa yang dibutuhkan di topologi jaringan?"
    menu:
        "A. Router atau Switch Layer 3 ✓":
            $ ch2_refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Tepat! Kamu butuh Inter-VLAN Routing yang dijalankan oleh Router (ROAS) atau Switch Layer 3."
            hide mentor with dissolve
        "B. Kabel straight-through khusus":
            show mentor tegas at right with dissolve
            mentor "❌ Kabel apa pun tidak akan bisa jika logikanya tidak diroutingkan antar Subnet."
            hide mentor with dissolve
        "C. Menambah jumlah Switch":
            show mentor tegas at right with dissolve
            mentor "❌ Menambah Switch L2 biasa tetap tidak akan merouting traffic antar Network / VLAN."
            hide mentor with dissolve
        "D. Kabel Crossover di server":
            show mentor tegas at right with dissolve
            mentor "❌ Salah. Bukan tentang jenis kabel, tapi fungsi Routing yang tidak dimiliki Switch Layer 2."
            hide mentor with dissolve

    ## SOAL 4
    narasi "── SOAL 4 ──────────────────────────────────────"
    narasi "Di saat terjadi serangan colok kabel dari MAC asing ke port lobby, fitur keamanan apa yang mencegahnya?"
    menu:
        "A. DHCP Server":
            show mentor tegas at right with dissolve
            mentor "❌ DHCP Server hanya memberikan IP, tidak memberikan keamanan proteksi port tingkat bawah."
            hide mentor with dissolve
        "B. Access Control List":
            show mentor tegas at right with dissolve
            mentor "❌ ACL bekerja di Layer 3 / Layer 4 untuk nge-filter IP dan Port. Keamanan Lapis 2 itu MAC."
            hide mentor with dissolve
        "C. Spanning Tree Protocol":
            show mentor tegas at right with dissolve
            mentor "❌ STP berguna menahan badai Broadcast Storm (looping), bukan pencurian akses tamu."
            hide mentor with dissolve
        "D. Switchport Port-Security ✓":
            $ ch2_refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Benar! Fitur Port-Security akan mendeteksi MAC address ilegal dan bisa otomatis Shutdown."
            hide mentor with dissolve

    ## SOAL 5
    narasi "── SOAL 5 ──────────────────────────────────────"
    narasi "Apakah kepanjangan dari VLAN?"
    menu:
        "A. Valid Local Area Network":
            show mentor tegas at right with dissolve
            mentor "❌ Valid bukan kata yang benar."
            hide mentor with dissolve
        "B. Virtual Local Area Network ✓":
            $ ch2_refleksi_score += 10
            show mentor senyum at right with dissolve
            mentor "✅ Benar! Virtual Local Area Network, karena pemisahannya dilakukan secara virtual di dalam Switch."
            hide mentor with dissolve
        "C. Very Large Area Network":
            show mentor tegas at right with dissolve
            mentor "❌ Jaringan luas biasa disebut WAN."
            hide mentor with dissolve
        "D. Variable Local Area Node":
            show mentor tegas at right with dissolve
            mentor "❌ Salah, kepanjanangannya Virtual Local Area Network."
            hide mentor with dissolve

    ## HASIL REFLEKSI CH2
    scene bg kantor with dissolve
    show mentor neutral at right with dissolve
    show rafi neutral at left with dissolve

    narasi ""
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    narasi "      HASIL REFLEKSI CHAPTER 2"
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    narasi ""
    narasi "Skor Refleksi: [ch2_refleksi_score] / 50 poin"

    if ch2_refleksi_score == 50:
        $ ch2_score += 20
        narasi "Nilai: ⭐⭐⭐ SEMPURNA! +20 bonus poin!"
        mentor "Pemahamanmu tentang VLAN mutlak! Kamu benar-benar pahlawan jaringan."
        rafi "[nama_mc] hebat banget! Nanti ajarin aku Router on a stick ya!"
    elif ch2_refleksi_score >= 30:
        $ ch2_score += 10
        narasi "Nilai: ⭐⭐ BAIK! +10 bonus poin!"
        mentor "Cukup bagus. Hanya butuh mempertajam sedikit logika Routing-nya saja."
    else:
        narasi "Nilai: ⭐ PERLU BELAJAR LAGI"
        mentor "Sepertinya Konsep Layer 2 belum matang sepenuhnya."
        mentor "Tapi jangan patah arang! Pelajari kembali materi Cisco CCNA di waktu luangmu."

    hide rafi with dissolve
    mentor "Sip, saatnya bersiap untuk tahap lebih kompleks. Jangkauan kantor kini semakin meluas."
    
    menu:
        "Lanjut ke Chapter 3: WAN & Firewall →":
            jump chapter3
            
        "Ulangi kuis refleksi Chapter 2":
            jump refleksi_quiz_ch2
            
        "Kembali ke Menu Utama":
            return

## ============================================================
## ─── CHAPTER 3: WAN, NAT, & SECURITY FIREWALL ───────────────
## ============================================================

label chapter3:
    play music "audio/bgm_main.mp3" fadein 1.5
    scene bg kantor with fade
    $ ch3_score = 0
    $ tries_ch3_q1 = 0
    $ tries_ch3_q2 = 0
    $ tries_ch3_q3 = 0
    $ tries_ch3_climax = 0

    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "       🌐  CHAPTER 3 DIMULAI  🌐"
    narasi "   WAN, Akses Publik, & Pertahanan Firewall"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    narasi "Bulan kedua magang di PT. Nusanet Teknologi..."
    
    show mentor neutral at right with dissolve
    show rafi neutral at left with dissolve
    
    mentor "Selamat pagi! Ada kabar gembira dan tantangan berat."
    mentor "Perusahaan kita baru saja menyewa gedung di kota seberang untuk dijadikan Kantor Cabang (Branch Office)."
    mentor "Selain itu, manajemen menuntut ada WiFi gratis di Lobby HQ untuk tamu yang berkunjung."
    
    rafi "WiFi tamu? Berarti siapapun bisa nyambung dari luar dong? Bahaya nggak tuh Pak?"
    mentor "Sangat bahaya! Jika tamu bisa menjangkau Server DB internal, bisa terjadi insiden kebocoran data."
    mentor "[nama_mc], tugasmu hari ini adalah ekspansi jaringan WAN sekaligus mengamankan Perimeter kita!"
    
    mc "Siap Pak Hendra! Dari mana kita akan mulai?"
    mentor "Routing Dinamis dari HQ ke Cabang."
    hide rafi
    hide mentor
    with dissolve
    
    jump ch3_quest1

## ─── CH3 QUEST 1: DYNAMIC ROUTING OSPF ──────────────────────
label ch3_quest1:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH3 QUEST 1: ROUTING OSPF KE CABANG ═══"
    mentor "Jika kita menghubungkan Router HQ dengan Router Branch, kita bisa saja menulis rute IP secara manual (Static Routing)."
    mentor "Tetapi, jika ada ratusan cabang, mendaftarkannya satu per satu sangat melelahkan."
    mentor "Protokol routing dinamis apa yang bisa menyesuaikan topologi, mempelajari rute otomatis, dan merupakan standar industri Open-Standard tercepat?"
    
label ch3_q1_pilih:
    $ tries_ch3_q1 += 1
    
    menu:
        "Static Routing":
            jump ch3_q1_salah_a
        "OSPF (Open Shortest Path First) ✓":
            jump ch3_q1_benar
        "RIP (Routing Information Protocol)":
            jump ch3_q1_salah_b
        "STP (Spanning Tree Protocol)":
            jump ch3_q1_salah_c
            
label ch3_q1_benar:
    $ ch3_score += 20
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    sistem "[[ ROUTER CONFIG ]] Router(config)# router ospf 1"
    sistem "[[ ROUTER CONFIG ]] Router(config-router)# network 192.168.10.0 0.0.0.255 area 0"
    sistem "[[ OSPF LOG ]] OSPF-5-ADJCHG: Process 1, Nbr 10.0.0.2 on Serial0/0/0 from LOADING to FULL, Loading Done"
    
    mc "OSPF, Pak! Algoritma link-state-nya sangat pintar mencari rute metrik tercepat (cost terkecil) jika ada router yang mati!"
    mentor "Excellent! OSPF menjadi sahabat terbaik perusahaan menengah ke atas. Rute otomatis terbentuk."
    mentor "+20 poin! Jaringan area cabang kini bisa saling PING ke HQ Office."
    jump ch3_quest2

label ch3_q1_salah_a:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "Static Routing membutuhkan kamu mengetik manual. Semakin banyak cabang, kamu akan pusing."
    mentor "Pilihlah sebuah 'Dynamic Routing Protocol' standar terbuka."
    if tries_ch3_q1 >= 3:
        mentor "Hint: Namanya Open Shortest Path First."
    jump ch3_q1_pilih

label ch3_q1_salah_b:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "RIP berbasis Hop-count rasanya sudah lawas. RIP lambat konvergensinya, dan maksimal 15 router (hop)."
    mentor "Cari yang berbasis Link-State."
    jump ch3_q1_pilih

label ch3_q1_salah_c:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "STP bukan routing protocol Layer 3, melainkan pengaman loop Layer 2 switch yang ada di Chapter 1."
    jump ch3_q1_pilih

## ─── CH3 QUEST 2: NAT (INTERNET GATEWAY) ────────────────────
label ch3_quest2:
    scene bg kantor with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH3 QUEST 2: NETWORK ADDRESS TRANSLATION ═══"
    show client panik at left with dissolve
    client "Loh, Pak! Saya kan tadi minta bagian Finance dihubungkan. Antar kantor cabang memang bisa ping, tapi saya GAK BISA AKSES GOOGLE!"
    mentor "IP lokal (Private) kita adalah 192.168.X.X. IP Ini tak bisa digunakan untuk navigasi di Internet publik."
    mentor "[nama_mc], bagaimana cara agar puluhan client kita bisa browsing ke public dengan 1 Public IP dari provider ISP kita?"
    
label ch3_q2_pilih:
    $ tries_ch3_q2 += 1
    menu:
        "Meminta ISP memberikan 100 IP Public tambahan.":
            jump ch3_q2_salah_a
        "Mengkonfigurasi NAT Overload (PAT) di Gateway Router. ✓":
            jump ch3_q2_benar
        "Menggunakan kabel Cross-Over dari PC ke internet.":
            jump ch3_q2_salah_b

label ch3_q2_benar:
    $ ch3_score += 20
    scene bg kantor with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    mc "Kita atur Network Address Translation (NAT) jenis Overload atau Port Address Translation (PAT) di Router Gateway, Pak!"
    mentor "Pilihan cerdas! NAT merubah IP Address pengirim (Private) menjadi IP Public kantor kita secara dinamis sebelum ke internet."
    
    sistem "[[ CONFIG ]] Router(config)# ip nat inside source list 1 interface GigabitEthernet0/1 overload"
    sistem "[[ STATUS ]] Internet Connection Established for 192.168.10.0/24 subnet"
    
    mentor "+20 Poin! Keluhan selesai, seluruh staf bisa browsing kembali."
    jump ch3_climax

label ch3_q2_salah_a:
    scene bg kantor with dissolve
    show mentor tegas at right with dissolve
    mentor "Beli IP Public tambahan itu mahal sekali! Jatah IP IPv4 juga sudah hampir habis."
    jump ch3_q2_pilih

label ch3_q2_salah_b:
    scene bg kantor with dissolve
    show mentor tegas at right with dissolve
    mentor "Kabel Cross-Over digunakan untuk PC ke PC atau Switch ke Switch. Internet butuh penterjemah IP Address."
    if tries_ch3_q2 >= 3:
        mentor "Hint: Butuh suatu metode Translasi atau Translation."
    jump ch3_q2_pilih

## ─── CH3 CLIMAX: FIREWALL & ACL ─────────────────────────────
label ch3_climax:
    play music "audio/bgm_trouble.mp3" fadein 1.0 volume 0.8
    scene bg serverroom with hpunch
    show screen hud_score
    
    narasi "═══ CH3 CLIMAX: FIREWALL INCIDENT ═══"
    show admin serius at right with hpunch
    show mentor tegas at left with dissolve
    
    sistem "[[ SYS WARNING ]] UNAUTHORIZED TELNET LOGIN ATTEMPT FROM 110.12.30.2!!"
    sistem "[[ SYS WARNING ]] CPU LOAD AT 99%% - BRUTE FORCE ATTACK DETECTED!"
    
    admin "Gawat! Server Database perusahaan diserang hacker dari internet menggunakan metode *Brute Force* Telnet di Port 23 secara terus menerus!"
    mentor "Serangan ini membuat CPU usage melonjak tinggi. Server akan 'Hanged'/Mati sebentar lagi!"
    mentor "[nama_mc], kita harus menyelamatkan server sebelum datanya bocor!"
    mentor "Tindakan pengamanan (Security Layer 3/4) apa yang bisa segera diaplikasikan pada Router kita untuk menangkal traffic serangan tersebut berdasarkan IP penyerang?"
    
label ch3_climax_pilih:
    $ tries_ch3_climax += 1
    menu:
        "Mematikan fungsi Firewall sepenuhnya.":
            jump ch3_climax_salah_b
        "Mencabut total koneksi internet perusahaan.":
            jump ch3_climax_salah_a
        "Pakai Access Control List (ACL) Extended! ✓":
            jump ch3_climax_benar

label ch3_climax_benar:
    $ ch3_score += 40
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    show admin happy at left with dissolve
    
    mc "Pakai Access Control List (ACL) Extended!"
    mc "Saya block secara spesifik Protocol TCP Port 23 (Telnet) dari 'ANY' (seluruh internet) yang menuju IP server kita, tapi biarkan sisa traffic operasional jalan."
    
    sistem "[[ ACTION ]] Router(config)# access-list 101 deny tcp any host 110.12.30.2 eq 23"
    sistem "[[ ACTION ]] Router(config)# access-list 101 permit ip any any"
    sistem "[[ ACTION ]] Router(config-if)# ip access-group 101 in"
    sistem "[[ SYS MONITOR ]] 990 matched packets dropped (Deny) ... Traffic normal kembali bersirkulasi."
    
    play music "audio/bgm_success.mp3" fadein 1.5
    admin "Astaga! Packet Drop berjalan! Konektivitas karyawan kembali hijau. Server Data terselamatkan!"
    mentor "Tindakan cepat yang mengagumkan, [nama_mc]! ACL adalah perpaduan dasar keamanan Firewall Layer 3/4."
    mentor "+40 Poin untuk refleks keamananmu!"
    jump ch3_ending

label ch3_climax_salah_a:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "Cabut internet? Operasional E-commerce dan seluruh Kantor Cabang ikutan mati! Kita rugi jutaan dolar!"
    mentor "Filter saja bad traffic-nya dengan Packet Filtering Router (ACL)."
    jump ch3_climax_pilih

label ch3_climax_salah_b:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "Menambah kerentanan Server? Bukannya diselamatkan kok firewallnya dimatikan?"
    mentor "Ayo cegat di gerbang utama / Router Gateway!"
    jump ch3_climax_pilih

## ─── CH3 ENDING ─────────────────────────────────────────────
label ch3_ending:
    hide screen hud_score
    scene bg kantor with dissolve
    
    show admin serius at right
    show mentor senyum at left with dissolve
    
    narasi "═══ CH3 EVALUASI ═══"
    mentor "Total skor [nama_mc] di Chapter 3 ini adalah: [ch3_score] poin."
    
    admin "Hari yang mendebarkan di meja Administrator Keamanan Jaringan. Namun, kamu menanggulanginya dengan tenang."
    
    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "          ★  CHAPTER 3 SELESAI  ★"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    narasi "🎓 Rekap Pembelajaran Chapter 3:"
    narasi "   ✓ Dynamic Routing (OSPF)"
    narasi "   ✓ Internet NAT Gateway Overload (PAT)"
    narasi "   ✓ Wi-Fi Security Encryption (WPA2/WPA3)"
    narasi "   ✓ Block Traffic using Access Control List (ACL) Extended Layer 4"
    narasi ""
    
    mentor "Luar Biasa, tapi sebelum merayakan..."
    mentor "Kuis Refleksi Akhir Chapter 3!!!"

    menu:
        "Lanjut ke Refleksi Chapter 3 →":
            jump refleksi_quiz_ch3

## ─── REFLEKSI KUIS CHAPTER 3 ────────────────────────────────
label refleksi_quiz_ch3:
    scene bg lab with dissolve
    $ ch3_refleksi_score = 0

    narasi ""
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"
    narasi "      REFLEKSI TOTAL — CHAPTER 3"
    narasi "   5 Nomor evaluasi ketahanan firewall!"
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"

    ## SOAL 1
    narasi "── SOAL 1 ──────────────────────────────────────"
    narasi "Metode penterjemahan IP Private menjadi IP Public sehingga bisa digunakan banyak client di sebut?"
    menu:
        "A. TCP":
            mentor "❌ Salah."
        "B. NAT Overload / PAT ✓":
            $ ch3_refleksi_score += 10
            mentor "✅ Benar!"
        "C. DNS":
            mentor "❌ DNS untuk mengubah Nama Domain jadi IP."
            
    ## SOAL 2
    narasi "── SOAL 2 ──────────────────────────────────────"
    narasi "Routing Dynamic manakah yang menggunakan mekanisme pertukaran metrik Cost/Link-State yang cepat?"
    menu:
        "A. Static":
            mentor "❌ Static adalah konfigurasi manual, bukan Dynamic."
        "B. OSPF ✓":
            $ ch3_refleksi_score += 10
            mentor "✅ Betul! Open Shortest Path First."
        "C. VLAN":
            mentor "❌ VLAN itu di switch, bukan routing protocol."
            
    ## SOAL 3
    narasi "── SOAL 3 ──────────────────────────────────────"
    narasi "Manakah dari berikut ini yang PENTING diterapkan pada Access Point public guest baru?"
    menu:
        "A. Membuka semua port jaringan internal.":
            mentor "❌ Bahaya! Pembobolan data."
        "B. Memisahkan VLAN dan menggunakan enkripsi WPA3 ✓":
            $ ch3_refleksi_score += 10
            mentor "✅ Sempurna! Isolasi traffic dan enkripsi kuat."
        "C. Mengaktifkan fitur auto-login untuk semua orang.":
            mentor "❌ Kurang tepat."
            
    ## SOAL 4
    narasi "── SOAL 4 ──────────────────────────────────────"
    narasi "Bila router mengolah rules pengecekan packet filtering berbasis Port & IP, fitur router apakah yang bekerja?"
    menu:
        "A. DHCP":
            mentor "❌ DHCP Server hanya mendistribusi IP."
        "B. Access Control List (ACL) ✓":
            $ ch3_refleksi_score += 10
            mentor "✅ Ya! Extended ACL pada layer 3 dan 4."
        "C. OSPF":
            mentor "❌ OSPF itu dinamis routing protocol."

    ## SOAL 5
    narasi "── SOAL 5 ──────────────────────────────────────"
    narasi "Apakah port default layanan Telnet yang kita block tadi pada Insiden Firewall?"
    menu:
        "A. Port 80 (HTTP)":
            mentor "❌ Itu untuk akses Web biasa."
        "B. Port 23 ✓":
            $ ch3_refleksi_score += 10
            mentor "✅ Benar! Port 23 biasa digunakan Telnet & sering jadi sasaran hacker karena trafficnya plaintext."
        "C. Port 443 (HTTPS)":
            mentor "❌ Aman terenkripsi, bukan default Telnet."

    ## EVALUASI SEMENTARA CH 3
    scene bg kantor with dissolve
    
    show admin happy at right, loncat
    show mentor senyum at left with dissolve
    show rafi neutral at center with dissolve

    narasi ""
    narasi "Skor Refleksi Tiga: [ch3_refleksi_score] / 50 poin"
    
    if ch3_refleksi_score == 50:
        $ ch3_score += 20
        admin "SEMPURNA! Jawaban mutlak sempurna di evaluasi Routing & Firewall!"
    elif ch3_refleksi_score >= 30:
        $ ch3_score += 10
        admin "LULUS! Keamanan firewall-mu cukup memadai."
    else:
        admin "Hmm... kamu harus banyak membaca ulang dokumentasi ACL Router."

    mentor "Tugas membangun Jaringan Area (WAN) dan Firewall sukses diselesaikan."
    mentor "Tetapi magangmu belum tamat. Tantangan berikutnya ada di sisi Server dan Layanan Komunikasi!"
    rafi "Waduh, ke ruang server Linux ya Pak? Ampun..."
    mc "Siap Pak Hendra! Server dan Layanan Voip, tantangan diterima!"
    
    menu:
        "Lanjut ke Chapter 4: Server & PBX →":
            jump chapter4
        "Ulangi Kuis Chapter 3":
            jump refleksi_quiz_ch3

## ============================================================
## ─── CHAPTER 4: SERVER ADMINISTRATOR & VOIP ─────────────────
## ============================================================

label chapter4:
    play music "audio/bgm_main.mp3" fadein 1.5
    scene bg serverroom with fade
    $ ch4_score = 0
    $ tries_ch4_q1 = 0
    $ tries_ch4_q2 = 0
    $ tries_ch4_climax = 0

    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "       🖥️  CHAPTER 4 DIMULAI  🖥️"
    narasi "   Sistem Server Dasar, DNS & Voice IP"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    
    show mentor neutral at right with dissolve
    show rafi neutral at left with dissolve

    mentor "Sebulan lagi magang berakhir. Infrastruktur router kita sudah mantap."
    mentor "Sekarang kita fokus ke level Aplikasi (Application Layer)."
    mentor "Admin IT kita, Pak Amin, butuh bantuan karena dia sedang cuti sakit."
    rafi "Asyik, kita yang kuasai ruang server sekarang."
    mentor "Jangan sembarangan tekan tombol, Rafi. Salah pencet, semua operasional stop."
    
    hide rafi with dissolve
    mentor "[nama_mc], bersiaplah menyeting Server!"
    jump ch4_quest1

## ─── CH4 QUEST 1: DNS & WEB SERVER ──────────────────────────
label ch4_quest1:
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH4 QUEST 1: DOMAIN NAME SYSTEM ═══"
    show client panik at left with dissolve
    client "Lho Pak! Katanya sistem absen perusahaan yang baru udah jalan di IP 192.168.10.50?"
    client "Karyawan mana hafal angka-angka begituan buat absen tiap pagi!"
    mentor "Benar Bu. Manusia lebih mudah mengingat nama daripada angka."
    hide client with dissolve
    
    mentor "[nama_mc], service layanan manakah di Linux Server yang memiliki peran untuk mengubah IP 192.168.10.50 menjadi nama 'absen.nusanet.local' saat diketik di Web Browser?"

label ch4_q1_pilih:
    $ tries_ch4_q1 += 1
    menu:
        "DHCP Server":
            jump ch4_q1_salah_a
        "File Server (Samba/FTP)":
            jump ch4_q1_salah_b
        "DNS Server (BIND9) ✓":
            jump ch4_q1_benar

label ch4_q1_benar:
    $ ch4_score += 20
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    sistem "[[ SERVER ROOT ]] root@server:~# systemctl restart bind9"
    sistem "[[ DNS CHECK ]] Resolving absen.nusanet.local... 192.168.10.50"
    
    mc "Jawabannya adalah DNS / Domain Name System Server, Pak! DNS berfungsi mentranslasikan domain huruf menjadi IP dan sebaliknya."
    mentor "Tepat sekali. Di Linux, software ini dikenal sebagai BIND9."
    mentor "+20 Poin. Sekarang klien bisa mengetik nama websitenya saja!"
    jump ch4_quest2

label ch4_q1_salah_a:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "DHCP (Dynamic Host Configuration Protocol) itu yang menyebarkan IP otomatis ke klien."
    mentor "Bukan untuk menterjemahkan nama Domain ke IP."
    jump ch4_q1_pilih

label ch4_q1_salah_b:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "File server hanya dipakai untuk *sharing folder*. Pikirkan sistem penamaan direktori IP internet."
    if tries_ch4_q1 >= 3:
        mentor "Hint: Namanya Domain Name System."
    jump ch4_q1_pilih

## ─── CH4 QUEST 2: VOIP & IP PBX ─────────────────────────────
label ch4_quest2:
    scene bg kantor with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH4 QUEST 2: VOICE OVER IP (TELEPON KANTOR) ═══"
    show admin serius at left with dissolve
    admin "Pak Hendra, tagihan telpon antar kantor ke cabang bulan ini bengkak sekali!"
    admin "Kita butuh telepon gratis dari meja ke meja menggunakan jaringan lokal LAN saja."
    mentor "Baik Pak, kami akan mengimplementasikan teknologi Telepon via Jaringan."
    hide admin with dissolve
    
    mentor "Untuk menghubungkan perangkat telepon IP antar meja (*IP Phone*), teknologi protokol dan Server Sentral apa yang umumnya digunakan pada industri jaringan?"

label ch4_q2_pilih:
    $ tries_ch4_q2 += 1
    menu:
        "SMTP (Email Server) / Postfix":
            jump ch4_q2_salah_a
        "VoIP (SIP) menggunakan IP PBX (Asterisk/Elastix) ✓":
            jump ch4_q2_benar
        "Video Graphics Array (VGA) / RDP":
            jump ch4_q2_salah_b

label ch4_q2_benar:
    $ ch4_score += 20
    scene bg kantor with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    sistem "[[ VOIP SERVER ]] SIP Extension 1001 ('[nama_mc]') Registered"
    sistem "[[ VOIP SERVER ]] SIP Extension 1002 ('Pak Hendra') Registered"
    sistem "[[ TELEPON ]] *KRING KRING* Panggilan masuk ke pesawat 1002 dari 1001..."
    
    mc "Kita gunakan teknologi VoIP (Voice over IP) berbasis protokol SIP, dibenamkan dalam server PABX seperti Asterisk!"
    mentor "Bagus! Kamu langsung ingat. Dengan sistem *IP PBX*, telepon bisa berjalan melalui kabel LAN biasa."
    mentor "+20 Poin! Kini kantor punya nomor *extension* internal pribadi."
    jump ch4_climax

label ch4_q2_salah_a:
    scene bg kantor with dissolve
    show mentor tegas at right with dissolve
    mentor "Itu buat email (surat menyurat), bukan untuk komunikasi Voice / Suara real-time."
    jump ch4_q2_pilih

label ch4_q2_salah_b:
    scene bg kantor with dissolve
    show mentor tegas at right with dissolve
    mentor "Itu hanya output Tampilan atau Remote Desktop. Dicari adalah sistem Telepon Sentral."
    jump ch4_q2_pilih

## ─── CH4 CLIMAX: WEB PROXY / FILTERING ──────────────────────
label ch4_climax:
    play music "audio/bgm_trouble.mp3" fadein 1.0 volume 0.8
    scene bg serverroom with hpunch
    show screen hud_score
    
    narasi "═══ CH4 CLIMAX: INSIDEN TENGGELAMNYA BANDWIDTH ═══"
    show admin serius at right with dissolve
    show mentor tegas at left with dissolve
    
    sistem "[[ ALERT ]] MAIN ROUTER CPU LOAD: 98%%"
    sistem "[[ ALERT ]] TRAFFIC ANOMALY: LAN PORT RX/TX PEAK (90Mbps)"
    
    admin "Ada apa ini?! Internet lumpuh total! Klien cabang komplain tidak bisa update stock data!"
    mentor "Sesuatu menyedot seluruh kapasitas internet kita secara masif dari dalam jaringan."
    
    show rafi malu at center with dissolve
    rafi "M-maaf Pak Hendra... Gue nemu file bajakan film 4K gratis di forum..."
    rafi "Sama anak-anak div lain kita download bareng pake PC kantor hehehe..."
    
    mentor "Rafi!!! Itu melanggar kebijakan perusahaan!"
    admin "Segera hentikan ini! Pastikan situs-situs film ilegal tidak bisa dituju!"
    hide admin
    hide rafi
    with dissolve
    
    mentor "[nama_mc], kita tidak bisa mencabut LAN. Kita butuh Layer 7 / Web Filtering!"
    mentor "Teknologi server Linux atau Mikrotik apa yang mampu *mencegat (intercept)* request URL halaman web dan memberlakuan drop/blokir ke domain nakal?"

label ch4_climax_pilih:
    $ tries_ch4_climax += 1
    menu:
        "Mematikan Browser Google Chrome di komputer karyawan.":
            jump ch4_climax_salah_a
        "NTP (Network Time Protocol) Server.":
            jump ch4_climax_salah_b
        "Web Proxy Server / Squid Proxy ✓":
            jump ch4_climax_benar

label ch4_climax_benar:
    $ ch4_score += 40
    scene bg serverroom with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    mc "Kita intercept requestnya sebelum pergi ke internet dengan *Web Proxy* Server! Seperti tool Squid Proxy di Linux atau Web Proxy di Mikrotik."
    mc "Tinggal pasang rule: drop url `*bioskopgratis*`!"
    
    sistem "[[ PROXY LOG ]] Setting up ACL dst-domain .bioskopgratis.org... DENY"
    sistem "[[ PROXY LOG ]] Redirecting Traffic ke Transparent Proxy Port 8080."
    sistem "[[ CLIENT VUE ]] ERROR 403: FORBIDDEN BY ADMINISTRATOR"
    
    play music "audio/bgm_success.mp3" fadein 1.5
    mentor "Akses mereka hangus terbakar *HTTP 403 Forbidden*! Trafik normal langsung kempes seketika."
    mentor "Luar biasa! Konfigurasi Web Proxy mencegah kebocoran bandwidth akibat pengguna usil."
    mentor "+40 Poin untuk solusi ini."
    jump ch4_ending

label ch4_climax_salah_a:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "Mereka akan menginstall browser lain, lagipula kita punya 100 PC. Jangan tangani manual dari sisi Client end-user!"
    mentor "Tangani dari hulu."
    jump ch4_climax_pilih

label ch4_climax_salah_b:
    scene bg serverroom with dissolve
    show mentor tegas at right with dissolve
    mentor "NTP Server itu untuk sinkronisasi Jam dan Tanggal di Server. Cari yang ada kata-kata Proxy."
    jump ch4_climax_pilih

## ─── CH4 ENDING ─────────────────────────────────────────────
label ch4_ending:
    hide screen hud_score
    scene bg kantor with dissolve
    show admin serius at right
    show mentor senyum at left with dissolve
    
    narasi "═══ CH4 EVALUASI ═══"
    mentor "Total skor [nama_mc] di Chapter 4 ini: [ch4_score] poin."
    admin "Pak Amin senang akhirnya ada junior yang membantu membenahi Server di bawah."
    
    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "          ★  CHAPTER 4 SELESAI  ★"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    narasi "🎓 Rekap Pembelajaran Chapter 4:"
    narasi "   ✓ Name Translation menggunakan DNS Server (BIND9)"
    narasi "   ✓ Voice Communication menggunakan VoIP / SIP (Asterisk)"
    narasi "   ✓ URL Filtering dengan Web Proxy Server (Layer 7)"
    narasi ""
    
    mentor "Sebelum masuk ke Bulan Final (Chapter 5)..."
    mentor "Mari ukur ketajaman pemahaman Aplikasi Komunikasimu."

    menu:
        "Lanjut ke Refleksi Chapter 4 →":
            jump refleksi_quiz_ch4

## ─── REFLEKSI KUIS CHAPTER 4 ────────────────────────────────
label refleksi_quiz_ch4:
    scene bg lab with dissolve
    $ ch4_refleksi_score = 0

    narasi ""
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"
    narasi "      REFLEKSI MATERI — CHAPTER 4"
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"

    ## SOAL 1
    narasi "── SOAL 1 ──────────────────────────────────────"
    narasi "Fitur/layanan yang bertugas melayani penerjemahan nama domain 'www.google.com' menjadi IP internet adalah?"
    menu:
        "A. DHCP":
            mentor "❌ Salah, DHCP membagi IP."
        "B. DNS ✓":
            $ ch4_refleksi_score += 10
            mentor "✅ Benar! Domain Name System."
        "C. FTP":
            mentor "❌ FTP File Transfer."

    ## SOAL 2
    narasi "── SOAL 2 ──────────────────────────────────────"
    narasi "Protokol standar industri yang banyak digunakan pada jaringan suara VoIP adalah?"
    menu:
        "A. TCP/UDP":
            mentor "❌ Terlalu mendasar."
        "B. SIP (Session Initiation Protocol) ✓":
            $ ch4_refleksi_score += 10
            mentor "✅ Bagus! SIP mendirikan sesi panggilan telepon suara."
        "C. HTTP":
            mentor "❌ Untuk format HTML (Web)."

    ## SOAL 3
    narasi "── SOAL 3 ──────────────────────────────────────"
    narasi "Jika kita menginstal Asterisk atau Briker ISO di sebuah PC Server, maka PC Server itu berubah fungsi menjadi?"
    menu:
        "A. Web Server Lokal":
            mentor "❌ Salah."
        "B. IP PBX atau Sentral Telepon VoIP ✓":
            $ ch4_refleksi_score += 10
            mentor "✅ Tepat! Asterisk adalah jantung IP-PBX open source."
        "C. Router Utama":
            mentor "❌ Asterisk tidak me-routing packet internet."

    ## SOAL 4
    narasi "── SOAL 4 ──────────────────────────────────────"
    narasi "Karyawan dilarang mengakses ekstensi '.mp4' atau '.iso' agar internet tidak lambat. Alat yang paling tepat menyaring itu adalah?"
    menu:
        "A. Switch Manageable":
            mentor "❌ Switch layer 2 tidak baca konten website."
        "B. Web Proxy (Clear-Text intercept) ✓":
            $ ch4_refleksi_score += 10
            mentor "✅ Tepat! Layer 7 Filtering Proxy."
        "C. Kabel UTP":
            mentor "❌ Hanya konduktor."

    ## SOAL 5
    narasi "── SOAL 5 ──────────────────────────────────────"
    narasi "Jika komputer lokal ingin langsung otomatis menerima IP Server Proxy tanpa menyetting di browser satu per satu disebut metode?"
    menu:
        "A. Ping":
            mentor "❌ Tidak relevan."
        "B. Transparent Proxy ✓":
            $ ch4_refleksi_score += 10
            mentor "✅ Benar! Transparent Proxy diam-diam meredirect port 80 ke 8080 tanpa sepengetahuan klien."
        "C. Traceroute":
            mentor "❌ Untuk melacak hop IP."

    ## HASIL CH4
    scene bg kantor with dissolve
    show mentor neutral at right with dissolve

    narasi ""
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    narasi "      HASIL REFLEKSI CHAPTER 4"
    narasi "      Skor: [ch4_refleksi_score] / 50 poin"
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    
    if ch4_refleksi_score == 50:
        $ ch4_score += 20
        mentor "Level Server Administration-mu mutlak hebat, [nama_mc]!"
    elif ch4_refleksi_score >= 30:
        $ ch4_score += 10
        mentor "Cukup tajam pemahaman Server-nya."
    else:
        mentor "Perlunya banyak mencoba installasi OS Linux Server di Virtual Box!"

    mentor "Sebentar lagi adalah hari penentuan evaluasimu."
    mentor "Persiapkan dirimu untuk ujian puncak di bulan kelima."
    
    menu:
        "Lanjut ke Final Chapter 5 →":
            jump chapter5
        "Ulangi kuis ini":
            jump refleksi_quiz_ch4

## ============================================================
## ─── CHAPTER 5: ADVANCED MANAGEMENT & DISASTER RECOVERY ─────
## ============================================================

label chapter5:
    play music "audio/bgm_main.mp3" fadein 1.5
    scene bg kantor with fade
    $ ch5_score = 0
    $ tries_ch5_q1 = 0
    $ tries_ch5_q2 = 0
    $ tries_ch5_climax = 0

    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "       👑  FINAL CHAPTER 5  👑"
    narasi "  Bandwidth, VPN, dan Disaster Recovery"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""

    show mentor neutral at right with dissolve
    show admin serius at left with dissolve

    mentor "Bulan terakhirmu magang di sini, [nama_mc]."
    mentor "Nusanet kini punya infrastruktur Router, Firewall, dan Server Lokal yang baik."
    admin "Ya, tetapi trafik harian menembus batas. Kita juga butuh jalur remote aman karena CEO kita bekerja di luar negeri minggu ini."
    
    mentor "Siap tempur? Kita akan menyempurnakan manajemen jaringan ini."
    jump ch5_quest1

## ─── CH5 QUEST 1: BANDWIDTH MANAGEMENT (QoS) ────────────────
label ch5_quest1:
    scene bg lab with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve
    
    narasi "═══ CH5 QUEST 1: QUALITY OF SERVICE (QoS) ═══"
    show rafi bingung at left with dissolve
    rafi "Suhu! Gawat suhu! Meeting Zoom petinggi perusahaan putus-putus!"
    rafi "Gue cek di trafik, anak-anak divisi Finance lagi narik file laporan bergiga-giga ke cloud!"
    mentor "Kalau jaringan dipenuhi file download besar, trafik real-time seperti Voice dan Video (UDP) akan drop."
    hide rafi

    mentor "[nama_mc], bagaimana cara mengatasi antrean agar traffic Zoom mendapat prioritas tinggi, sedangkan download file dilimit kecepatannya (Traffic Shaping)?"

label ch5_q1_pilih:
    $ tries_ch5_q1 += 1
    menu:
        "Memperbesar Pipa Kabel Fiber Optic pakai solatip.":
            jump ch5_q1_salah_a
        "Membagikan jaringan VLAN baru per orang.":
            jump ch5_q1_salah_b
        "Menggunakan Simple Queue Mikrotik / QoS. ✓":
            jump ch5_q1_benar

label ch5_q1_benar:
    $ ch5_score += 20
    scene bg lab with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    sistem "[[ MIKROTIK ]] /queue simple add name='Limit_Finance' target=192.168.20.0/24 max-limit=5M/5M"
    sistem "[[ TRAFFIC MONITOR ]] Finance Download: 5.0 Mbps (Capped). Zoom Meeting: Smooth (0 Packet Loss)."
    
    mc "Kita limit bandwidth divisi Finance dan pasang Quality of Service (QoS) Priority untuk Zoom pakai Simple Queue, Pak!"
    mentor "Sempurna! Manajemen Bandwidth memastikan 'fairness' pemakaian trafik internet agar tidak ada yang menang sendiri."
    mentor "+20 Poin! Meeting CEO aman sejahtera tanpa lag."
    jump ch5_quest2

label ch5_q1_salah_a:
    scene bg lab with dissolve
    show mentor tegas at right with dissolve
    mentor "Bandwidth tidak bisa ditambah secara fisik dengan solatip! Kita berlangganan kecepatan fix ke ISP."
    jump ch5_q1_pilih

label ch5_q1_salah_b:
    scene bg lab with dissolve
    show mentor tegas at right with dissolve
    mentor "VLAN memisahkan broadcast domain, tapi kecepatan internet (Bandwidth) yang ditarik tetap akan rebutan dan saling menyedot."
    if tries_ch5_q1 >= 3:
        mentor "Hint: Butuh suatu 'Queue' (Antrean) atau Limitasi."
    jump ch5_q1_pilih

## ─── CH5 QUEST 2: VIRTUAL PRIVATE NETWORK (VPN) ─────────────
label ch5_quest2:
    scene bg kantor with dissolve
    show screen hud_score
    show mentor neutral at right with dissolve

    narasi "═══ CH5 QUEST 2: REMOTE ACCESS VPN ═══"
    show admin serius at left with dissolve
    admin "CEO sudah di luar negeri. Beliau butuh menarik file laporan keuangan rahasia dari Server internal (192.168.10.10)."
    admin "Tetapi server ini kita 'isolasi' tidak punya IP Publik agar aman."
    hide admin
    
    mentor "Internet hotel tempat CEO menginap itu jaringan publik yang tidak terpercaya."
    mentor "Teknologi apa yang harus kita pasang di Router Nusanet agar CEO bisa seolah-olah 'berada' di dalam ruang LAN kantor dengan sambungan terenkripsi?"

label ch5_q2_pilih:
    $ tries_ch5_q2 += 1
    menu:
        "Membuat lorong Virtual Private Network (VPN). ✓":
            jump ch5_q2_benar
        "Menyuruh CEO mem-flashdisk datanya.":
            jump ch5_q2_salah_a
        "Menggunakan Bluetooth dari beda benua.":
            jump ch5_q2_salah_b

label ch5_q2_benar:
    $ ch5_score += 20
    scene bg kantor with dissolve
    show screen hud_score
    show mentor senyum at right with dissolve
    
    sistem "[[ VPN SERVER ]] Incoming L2TP/IPSec Connection from 203.0.113.5 (CEO_Macbook)"
    sistem "[[ VPN TUNNEL ]] Assigned Virtual IP: 192.168.99.2. Status: SECURED & ENCRYPTED"
    
    mc "Kita buka layanan Remote Access VPN (seperti OpenVPN atau L2TP/IPSec), Pak!"
    mentor "Bagus sekali! Dengan VPN, trafik data terenkripsi *tunneling* melewati internet publik menjangkau IP Private lokal kita."
    mentor "CEO sekarang bisa membuka file Share Samba dari kamar hotelnya."
    mentor "+20 Poin! Remote worker terfasilitasi aman!"
    jump ch5_climax

label ch5_q2_salah_a:
    scene bg kantor with dissolve
    show mentor tegas at right with dissolve
    mentor "CEO-nya sudah di Eropa! Masa mau kesini naik pesawat hanya untuk nyolok flashdisk?"
    jump ch5_q2_pilih

label ch5_q2_salah_b:
    scene bg kantor with dissolve
    show mentor tegas at right with dissolve
    mentor "Jarak tempuh frekuensi Bluetooth itu cuma 10 Meter! Mikir ah!"
    jump ch5_q2_pilih

## ─── CH5 CLIMAX: DISASTER RECOVERY & RANSOMWARE ─────────────
label ch5_climax:
    play music "audio/bgm_trouble.mp3" fadein 1.0 volume 0.8
    scene bg serverroom with hpunch
    show screen hud_score
    
    narasi "═══ FINAL CLIMAX: DISASTER RECOVERY PROTOCOL ═══"
    show admin serius at right with hpunch
    show mentor tegas at left with dissolve
    
    sistem "[[ SYSTEM ALERT ]] RANSOMWARE ENCRYPTION DETECTED ON PC-FINANCE-3!"
    sistem "[[ SYSTEM ALERT ]] CORE ROUTER MAIN CONFIGURATION CORRUPTED!"
    
    admin "Kiamat! Kiamat Jaringan! PC divisi Keuangan disusupi *Ransomware* dari email phising!"
    mentor "File-share lokal mulai terenkripsi jadi `.locked`!"
    
    admin "Belum cukup itu, karena panik, staf magang sebelahnya nendang kabel power Router Utama saat dia nulis memori. Router nge-wipe total jadi Factory Default!!"
    
    mentor "Internet mati! Jaringan terputus dari cabang! Dan Ransomware liar sebentar lagi menjalar ke Server Utama!"
    mentor "[nama_mc]! Ini adalah insting terpenting dari seorang Network Engineer!"
    mentor "Apa LANGKAH PERTAMA (Aksi Fisik Layer 1) dan LANGKAH KEDUA (Pemulihan Router) yang harus kita lakukan DALAM 30 DETIK INI?!"

label ch5_climax_pilih:
    $ tries_ch5_climax += 1
    menu:
        "Matikan PC Finance-3 secara paksa, lalu nangis bersama.":
            jump ch5_climax_salah_a
        "1. Cabut kabel LAN PC Finance dari dinding. 2. Restore file backup (.rsc) ke Router lokal! ✓":
            jump ch5_climax_benar
        "Format ulang seluruh Hardisk Server Utama.":
            jump ch5_climax_salah_b

label ch5_climax_benar:
    $ ch5_score += 40
    scene bg serverroom with hpunch
    show screen hud_score
    show mentor senyum at left with dissolve
    show admin happy at right with dissolve
    
    mc "CABUT DULU KABEL LAN PC-FINANCE-3 SECARA FISIK SEKARANG! Isolasi penyebaran Malware!"
    mc "Selanjutnya saya akan flash Router Utama dengan file 'backup-monthly.rsc' yang sudah rutin saya simpan sejak Chapter 1!"
    
    sistem "[[ ACTION ]] *PLUG OUT* LAN CABLE PORT 6. Ransomware Isolated."
    sistem "[[ ROUTER RECOVERY ]] Importing 'backup-monthly.rsc'..."
    sistem "[[ ROUTER RECOVERY ]] Loading VLAN, Routing, NAT, Firewall Rules... DONE."
    
    play music "audio/bgm_success.mp3" fadein 1.5
    admin "Trafik inter-VLAN nyala! Internet nyala! Ransomware berhenti menyebar!"
    mentor "Menyelamatkan miliaran aset dalam 30 detik! Isolasi infeksi (*Containment*) adalah hukum pertama Incident Response."
    mentor "Dan kamu sadar pentingnya Sistem *Backup & Restore*."
    mentor "+40 Poin Masterpiece!"
    jump ch5_ending

label ch5_climax_salah_a:
    scene bg serverroom with hpunch
    show mentor tegas at left with dissolve
    mentor "Nangis tidak akan merecover Router yang reset Factory! Cepat cabut koneksinya dan kembalikan backup konfigurasi Router!"
    jump ch5_climax_pilih

label ch5_climax_salah_b:
    scene bg serverroom with hpunch
    show mentor tegas at left with dissolve
    mentor "Server Utama belum terinfeksi 100%%! Jangan diformat, datanya hilang semua!"
    mentor "Putuskan saja dulu koneksi fisik pasien sumber penyakitnya (Layer 1)!"
    jump ch5_climax_pilih

## ─── CH5 ENDING (GRAND FINALE) ──────────────────────────────
label ch5_ending:
    hide screen hud_score
    scene bg kantor with dissolve
    show admin serius at right
    show mentor senyum at left with dissolve
    
    narasi "═══ CH5 EVALUASI AKHIR ═══"
    mentor "Total skor [nama_mc] di Final Chapter 5 ini: [ch5_score] poin."
    
    narasi ""
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi "          ★  MAGANG SELESAI  ★"
    narasi "✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦"
    narasi ""
    narasi "🎓 Rekap Kepakaran Chapter 5:"
    narasi "   ✓ Bandwidth Management & QoS"
    narasi "   ✓ Remote Access VPN (Tunneling Terenkripsi)"
    narasi "   ✓ Disaster Recovery & Malware Physical Containment"
    narasi ""
    
    admin "Masa 5 bulan berlalu begitu cepat."
    mentor "Sebelum kami menerbitkan rapor akhirmu dan menyerahkan Sertifikat Teknisi Jaringan Senior..."
    mentor "Ujian Komprehensif Pamungkas (5 Soal Terakhir) dimulai SEKARANG!"

    menu:
        "Masuk ke Kuis Grand Final Chapter 5 →":
            jump refleksi_quiz_ch5

## ─── REFLEKSI KUIS CHAPTER 5 ────────────────────────────────
label refleksi_quiz_ch5:
    scene bg lab with dissolve
    $ ch5_refleksi_score = 0

    narasi ""
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"
    narasi "      UJIAN KOMPREHENSIF FINAL"
    narasi "📝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📝"

    ## SOAL 1
    narasi "── SOAL FINAL 1 ──────────────────────────────────────"
    narasi "Teknologi yang digunakan agar data video call mendapatkan akses cepat didahulukan ketimbang data download biasa adalah?"
    menu:
        "A. Simple Queue / Quality of Service (QoS) ✓":
            $ ch5_refleksi_score += 10
            mentor "✅ Benar! QoS mengatasi *bottleneck*."
        "B. RIPV2":
            mentor "❌ Salah, itu routing protocol."
        "C. SMTP":
            mentor "❌ SMTP adalah email antar server."

    ## SOAL 2
    narasi "── SOAL FINAL 2 ──────────────────────────────────────"
    narasi "Protokol yang paling aman dan populer digunakan untuk kebutuhan Virtual Private Network (VPN) terenkripsi adalah?"
    menu:
        "A. Telnet":
            mentor "❌ Tidak terenkripsi."
        "B. OpenVPN / L2TP IPSec ✓":
            $ ch5_refleksi_score += 10
            mentor "✅ Bagus! IPSec memastikan confidentiality tunnel VPN."
        "C. PING":
            mentor "❌ Ping sebatas mengecek reachability IP."

    ## SOAL 3
    narasi "── SOAL FINAL 3 ──────────────────────────────────────"
    narasi "Saat terdeteksi pergerakan file ransomware di ujung PC lantai 5, tindakan pertama yang wajib dilakukan staf IT adalah?"
    menu:
        "A. Segera isolasi komputer tersebut dari jaringan luar dengan mencabut kabel LAN/Disable Interface. ✓":
            $ ch5_refleksi_score += 10
            mentor "✅ Tepat! *Containment* (menghentikan sebaran lateral malware) adalah hal wajib di cyber security respons."
        "B. Menghapus folder System32.":
            mentor "❌ Membunuh Windows PC tersebut sepenuhnya."
        "C. Mengganti casing komputer.":
            mentor "❌ Gak logis."

    ## SOAL 4
    narasi "── SOAL FINAL 4 ──────────────────────────────────────"
    narasi "Mengapa seorang SysAdmin Jaringan sangat mendambakan mekanisme Backup file konfigurasi seperti .rsc atau .cfg?"
    menu:
        "A. Untuk menyombongkan keahlian ke teman.":
            mentor "❌ Bukan."
        "B. Upaya pemulihan massal (Disaster Recovery) cepat untuk jaringan yang mati total. ✓":
            $ ch5_refleksi_score += 10
            mentor "✅ Sempurna. Administrasi jaringan tanpa backup berkala sama dengan menunggu kiamat lokal."
        "C. Supaya internet lebih cepat.":
            mentor "❌ Backup tidak membuat internet cepat."

    ## SOAL 5
    narasi "── SOAL FINAL 5 ──────────────────────────────────────"
    narasi "Dari Layer 1 (Fisik) ke Layer 7 (Aplikasi), di layer manakah Web Proxy Server (Squid) bekerja untuk membaca nama situs ilegal?"
    menu:
        "A. Layer 1 (Physical)":
            mentor "❌ Fisik hanya sinyal biner dan listrik."
        "B. Layer 7 (Application) ✓":
            $ ch5_refleksi_score += 10
            mentor "✅ LUAR BIASA! Layer 7 bertugas memproses antarmuka aplikasi dan protokol konten berlevel HTTP/Website."
        "C. Layer 3 (Network)":
            mentor "❌ Layer 3 memproses IP routing (seperti OSPF)."

    ## HASIL AKHIR & GRAND FINALE
    scene bg ending_ok with dissolve
    play music "audio/bgm_success.mp3" fadein 2.0
    
    show admin happy at right, loncat
    show mentor senyum at left with dissolve
    show rafi neutral at center with dissolve

    narasi ""
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    narasi "      HASIL UJIAN KOMPREHENSIF"
    narasi "      Skor Akhir: [ch5_refleksi_score] / 50 poin"
    narasi "📊━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━📊"
    
    if ch5_refleksi_score == 50:
        $ ch5_score += 50
        admin "SEMPURNA!! Nilai 100 di ujian puncak!"
    elif ch5_refleksi_score >= 30:
        $ ch5_score += 30
        admin "Kamu LULUS Ujian Komprehensif dengan nilai memuaskan."
    else:
        admin "Kamu memiliki potensi besar, meskipun ada beberapa nilai evaluasi yang rendah."

    mentor "Masa magang [nama_mc] resmi berakhir hari ini. Keterampilan yang kamu tempa mulai dari kabel fisik (Crimping), administrasi Switch (VLAN), pengamanan gerbang (Firewall), perakitan (Server), hingga pelimitasi (QoS) sudah tingkat Profesional!"
    
    rafi "Selamat cuy! Jangan lupakan gue kalau lu sukses duluan ya!"
    
    admin "Sebagai penghargaan atas upaya luar biasamu..."
    admin "Maukah kamu menerima posisi Kontrak Junior Network Engineer *Full-Time* di Nusanet Teknologi?"
    
    mc "Tentu saja, Bapak! Terima kasih atas ilmunya!"
    
    narasi "   「 NetPro: Magang Jaringan — TRUE ENDING COMPLETED!!! 」"
    
    menu:
        "Mainkan Lagi (Dari awal Chapter 1)":
            jump start
        "Keluar dari Permainan (Quit)":
            return


