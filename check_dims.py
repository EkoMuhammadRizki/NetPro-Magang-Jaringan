import struct

def get_image_dims(path):
    with open(path, 'rb') as f:
        data = f.read(24)
        if data[0:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>LL', data[16:24])
            return w, h
    return None

files = [
    "game/gui/MulaiButton.png",
    "game/gui/LanjutkanButton.png",
    "game/gui/KeluarButton.png"
]

for f in files:
    try:
        print(f"{f}: {get_image_dims(f)}")
    except Exception as e:
        print(f"{f}: Error {e}")
