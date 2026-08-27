import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix the CSS block
css_block = """    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            background-color: #3e4e3b;
            color: #e9e9e9;
        }
        h1, h2, h3, h4, h5, h6, .serif {
            font-family: 'Cormorant Garamond', serif;
        }
        .bg-olive { background-color: #3e4e3b; }
        .text-olive { color: #3e4e3b; }
        .bg-sage { background-color: #7f886f; }
        .text-sage { color: #7f886f; }
        .bg-dark-green { background-color: #013b23; }
        .text-dark-green { color: #013b23; }

        /* Boarding Pass Styles */
        .boarding-pass {
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            background: #fff;
            position: relative;
        }
        @media(min-width: 768px) {
            .boarding-pass {
                flex-direction: row;
            }
        }
        .bp-left {
            flex: 1;
            padding: 2.5rem;
            border-bottom: 2px dashed #e5e7eb;
            position: relative;
        }
        @media(min-width: 768px) {
            .bp-left {
                border-bottom: none;
                border-right: 2px dashed #e5e7eb;
            }
        }
        .bp-right {
            padding: 2.5rem;
            background: #fafafa;
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        @media(min-width: 768px) {
            .bp-right {
                width: 280px;
            }
        }
        
        .cutout-top-dark, .cutout-bottom-dark {
            position: absolute;
            width: 40px;
            height: 40px;
            background-color: #3e4e3b;
            border-radius: 50%;
            z-index: 10;
        }
        /* Hide cutouts on mobile for cleaner look, show on desktop */
        @media(max-width: 767px) {
            .cutout-top-dark, .cutout-bottom-dark { display: none; }
        }
        @media(min-width: 768px) {
            .cutout-top-dark { right: -21px; top: -20px; }
            .cutout-bottom-dark { right: -21px; bottom: -20px; }
        }

        .barcode {
            font-family: 'Libre Barcode 39', cursive;
            font-size: 3.5rem;
            line-height: 1;
            color: #3e4e3b;
        }
        
        /* Smooth Scroll */
        html { scroll-behavior: smooth; }
    </style>"""

html = re.sub(r'<style>.*?</style>', css_block, html, flags=re.DOTALL)

# Let's also fix the timeline placeholder image block, which had text-white/70 changed to text-white/70 italic incorrectly if they got duplicated
# No, it's fine. 

with open('index.html', 'w') as f:
    f.write(html)
