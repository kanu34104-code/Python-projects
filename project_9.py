7. #Convert Text to Handwriting
import pywhatkit as pw
from PIL import Image, ImageDraw, ImageFont

# Text to convert
txt = """Python is an interpreted, high-level and general-purpose programming language.
Python's design philosophy emphasizes code readability with its notable use of significant whitespace."""

try:
    print("🖋️ Trying with pywhatkit online API...")
    pw.text_to_handwriting(txt, "demo.png", [0, 0, 138])
    print("✅ Image created successfully using pywhatkit!")

except Exception as e:
    print("⚠️ pywhatkit failed due to:", e)
    print("🧠 Switching to offline Pillow method...")

    try:
        # Create blank white image
        img = Image.new('RGB', (800, 400), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        # Load font (replace with handwriting-style font if you have one)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        # Draw text in dark blue ink color
        draw.text((20, 20), txt, fill=(0, 0, 138), font=font)

        # Save as PNG
        img.save("demo.png")
        print("✅ Image created successfully using offline Pillow method!")

    except Exception as inner_e:
        print("❌ Failed to create image:", inner_e)

print("END")
