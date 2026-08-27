import os
from PIL import Image, ImageDraw, ImageFont

media_dir = '_assets/media'
images = []
labels = []

for d in [media_dir, '_assets/images', '.']:
    if not os.path.exists(d): continue
    for f in os.listdir(d):
        path = os.path.join(d, f)
        if f.endswith('.png') or f.endswith('.jpg'):
            try:
                img = Image.open(path).convert('RGBA')
                img.thumbnail((300, 300))
                images.append(img)
                labels.append(f)
            except Exception as e:
                pass

cols = 5
rows = (len(images) + cols - 1) // cols
cell_w = 350
cell_h = 350
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
    draw.text((x + 10, y + cell_h - 20), label[:15], fill=(0,0,0))

collage.save('collage2.png')
print("Collage saved as collage2.png")
