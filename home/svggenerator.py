import subprocess

# Set the dimensions of the SVG image
width = 300
height = 190

# Create an Inkscape SVG file with a rectangle as the background
svg_content = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="{width}" height="{height}" fill="lightblue" />
</svg>
'''

# Save the SVG content to a file
with open('background.svg', 'w') as f:
    f.write(svg_content)

print("SVG background image generated as 'background.svg'.")
