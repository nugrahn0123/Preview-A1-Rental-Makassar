import io
from rembg import remove
from PIL import Image

for n in ["Veloz", "BRV", "Honda HRV"]:
    src = f"img/{n}.jpg"
    dst = f"img/{n}.png"
    with open(src, "rb") as f:
        out = remove(f.read())
    Image.open(io.BytesIO(out)).save(dst)
    print("OK", dst)
