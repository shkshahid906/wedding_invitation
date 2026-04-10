from PIL import Image
import os

INPUT_FOLDER = "curtain"
OUTPUT_FOLDER = "compressed"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

QUALITY = 50  # 🔥 best for web

EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(EXTENSIONS):

        input_path = os.path.join(INPUT_FOLDER, filename)

        # 🔥 change extension to .webp
        new_name = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(OUTPUT_FOLDER, new_name)

        try:
            img = Image.open(input_path)

            # Fix transparency
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # ✅ SAVE AS WEBP (THIS IS THE MAGIC)
            img.save(output_path, "WEBP", quality=QUALITY, method=6)

            print(f"✅ Compressed: {filename} → {new_name}")

        except Exception as e:
            print(f"❌ Error: {filename} → {e}")