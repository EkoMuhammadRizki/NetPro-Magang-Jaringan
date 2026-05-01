import struct

def get_image_dims(path):
    """
    Fungsi untuk mengambil dimensi (lebar & tinggi) dari file gambar PNG secara manual.
    Membaca header file PNG untuk mendapatkan informasi ukuran.
    """
    with open(path, 'rb') as f:
        data = f.read(24)
        if data[0:8] == b'\x89PNG\r\n\x1a\n': # Cek apakah ini file PNG valid
            w, h = struct.unpack('>LL', data[16:24])
            return w, h
    return None

# Daftar file yang ingin dicek dimensinya
files = [
    "game/gui/MulaiButton.png",
    "game/gui/LanjutkanButton.png",
    "game/gui/KeluarButton.png"
]

# Melakukan perulangan untuk setiap file dan mencetak hasilnya
for f in files:
    try:
        print(f"{f}: {get_image_dims(f)}")
    except Exception as e:
        print(f"{f}: Error {e}")
