import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Navbar logo replacement
navbar_old = '<img src="tat.png" alt="Icon" class="h-10 w-10 object-contain group-hover:scale-110 transition-transform duration-300">'
navbar_new = '''<div class="relative h-10 w-10 flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
            <img src="_assets/media/33c69b1d1a33662e6ee76d058a7d172a.svg" class="absolute inset-0 w-full h-full brightness-0 invert opacity-80" alt="Mountain">
            <img src="_assets/media/a3f24207773fb7235aa84642c26a6661.svg" class="absolute bottom-1 w-5 h-5 z-10 brightness-0 invert" alt="Couple">
        </div>'''
html = html.replace(navbar_old, navbar_new)

# 2. Timeline placeholder icon replacement
timeline_old = '<img src="tat.png" class="w-16 h-16 opacity-50 mb-4" alt="Icon">'
timeline_new = '''<div class="relative w-16 h-16 mb-4 opacity-70">
                         <img src="_assets/media/33c69b1d1a33662e6ee76d058a7d172a.svg" class="absolute inset-0 w-full h-full brightness-0 invert" alt="Mountain">
                         <img src="_assets/media/a3f24207773fb7235aa84642c26a6661.svg" class="absolute bottom-2 left-1/2 transform -translate-x-1/2 w-8 h-8 z-10 brightness-0 invert" alt="Couple">
                    </div>'''
html = html.replace(timeline_old, timeline_new)

# 3. Boarding pass icon replacement
bp_old = '<img src="tat.png" alt="Icon" class="w-14 h-14 opacity-90 drop-shadow-sm">'
bp_new = '''<div class="relative w-14 h-14 opacity-90 drop-shadow-sm">
                        <img src="_assets/media/33c69b1d1a33662e6ee76d058a7d172a.svg" class="absolute inset-0 w-full h-full" alt="Mountain">
                        <img src="_assets/media/a3f24207773fb7235aa84642c26a6661.svg" class="absolute bottom-1 left-1/2 transform -translate-x-1/2 w-6 h-6 z-10" alt="Couple">
                    </div>'''
html = html.replace(bp_old, bp_new)

# 4. Footer icon replacement
footer_old = '<img src="tat.png" alt="Tatiana & Majd" class="w-20 h-20 mx-auto mb-10 opacity-90">'
footer_new = '''<div class="relative w-20 h-20 mx-auto mb-10 opacity-90">
            <img src="_assets/media/33c69b1d1a33662e6ee76d058a7d172a.svg" class="absolute inset-0 w-full h-full brightness-0 invert opacity-80" alt="Mountain">
            <img src="_assets/media/a3f24207773fb7235aa84642c26a6661.svg" class="absolute bottom-2 left-1/2 transform -translate-x-1/2 w-10 h-10 z-10 brightness-0 invert" alt="Couple">
        </div>'''
html = html.replace(footer_old, footer_new)

with open('index.html', 'w') as f:
    f.write(html)
