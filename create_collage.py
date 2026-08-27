import os
import cairosvg
from PIL import Image, ImageDraw, ImageFont

media_dir = '_assets/media'
images = []
labels = []

# Process SVGs and convert to PNG in memory or temp
for f in os.listdir(media_dir):
    path = os.path.join(media_dir, f)
    try:
        if f.endswith('.svg'):
            out_path = f'/tmp/{f}.png'
            cairosvg.svg2png(url=path, write_to=out_path, parent_width=200, parent_height=200)
            img = Image.open(out_path).convert('RGBA')
            images.append(img)
            labels.append(f)
        elif f.endswith('.png') or f.endswith('.jpg'):
            img = Image.open(path).convert('RGBA')
            img.thumbnail((200, 200))
            images.append(img)
            labels.append(f)
    except Exception as e:
        pass

if not images:
    print("No images found.")
    exit(0)

# Create a collage
cols = 4
rows = (len(images) + cols - 1) // cols
cell_w = 250
cell_h = 250
collage = Image.new('RGB', (cols * cell_w, rows * cell_h), (255, 255, 255))
draw = ImageDraw.Draw(collage)

for i, (img, label) in enumerate(zip(images, labels)):
    r = i // cols
    c = i % cols
    x = c * cell_w
    y = r * cell_h
    
    # paste image centered
    ix = x + (cell_w - img.width) // 2
    iy = y + (cell_h - 20 - img.height) // 2
    collage.paste(img, (ix, iy), img)
    
    # draw label
    draw.text((x + 10, y + cell_h - 20), label, fill=(0,0,0))

collage.save('collage.png')
print("Collage saved as collage.png")
