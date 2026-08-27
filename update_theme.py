import re

with open('index.html', 'r') as f:
    html = f.read()

# Body background
html = html.replace('background-color: #f7f8f5;', 'background-color: #3e4e3b;')
html = html.replace('color: #3e4e3b;', 'color: #e9e9e9;')

# Navbar
html = html.replace('bg-[#f7f8f5]/90', 'bg-[#3e4e3b]/90')
html = html.replace('bg-[#f7f8f5]/95', 'bg-[#3e4e3b]/95')
html = html.replace('text-olive tracking-wider', 'text-[#e9e9e9] tracking-wider')
html = html.replace('after:bg-olive', 'after:bg-[#e9e9e9]')
html = html.replace('hover:text-olive', 'hover:text-white')

# Timeline / Our Story
html = html.replace('bg-white', 'bg-transparent', 1) # First occurrence is our-story section
html = html.replace('text-olive mb-6', 'text-white mb-6') # 10 years of us
html = html.replace('text-olive mb-3', 'text-[#e9e9e9] mb-3') # 2017, 2025, 2027
html = html.replace('text-gray-500 text-lg', 'text-white/70 text-lg')
html = html.replace('group-hover:bg-olive', 'group-hover:bg-[#e9e9e9]')

# Timeline placeholder wedding block
html = html.replace('bg-[#f7f8f5] w-full h-80', 'bg-[#3e4e3b] border border-white/10 w-full h-80')
html = html.replace('text-olive/70 italic', 'text-white/70 italic')
html = html.replace('group-hover:border-olive/30', 'group-hover:border-white/30')

# Save the Date Section (was bg-olive)
# We can leave it as bg-olive, but since body is bg-olive, we could add a subtle divider or just keep it
html = html.replace('bg-olive text-white', 'bg-transparent text-white')
html = html.replace('border-sage/40', 'border-white/20')

# Boarding Pass Section
html = html.replace('bg-[#f7f8f5] px-6', 'bg-transparent px-6') # section bg
html = html.replace('text-olive mb-4', 'text-white mb-4') # Your invitation
html = html.replace('cutout-top', 'cutout-top-dark')
html = html.replace('cutout-bottom', 'cutout-bottom-dark')
html = html.replace('background-color: #f7f8f5;\n            border-radius: 50%;', 'background-color: #3e4e3b;\n            border-radius: 50%;')
# Make the ticket background white
html = html.replace('bg-[#f7f8f5] px-3', 'bg-white px-3')

# Footer
html = html.replace('bg-white py-24', 'bg-transparent py-24')
html = html.replace('text-olive mb-6', 'text-white mb-6')
html = html.replace('border-gray-100', 'border-white/10')
html = html.replace('text-gray-400', 'text-white/40')
html = html.replace('bg-gray-300', 'bg-white/20')

with open('index.html', 'w') as f:
    f.write(html)
