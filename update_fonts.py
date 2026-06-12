import re

with open('page.html', 'r') as f:
    content = f.read()

# Replace Google Fonts link
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Dongle:wght@300;400;700&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap" rel="stylesheet">'
)

# Replace font-family
content = content.replace("'Dongle'", "'Montserrat'")

# Scale down font-sizes
def scale_font(match):
    size = int(match.group(1))
    # Dongle is approx 1.8x larger than Montserrat visually, so divide by 1.8
    new_size = max(10, round(size / 1.7))
    return f"font-size: {new_size}px"

content = re.sub(r'font-size:\s*(\d+)px', scale_font, content)

# Specific tweaks for the new template
# 1. Main Nav border and spacing
content = content.replace(
    '.main-nav {\n            display: flex;',
    '.main-nav {\n            display: flex;\n            border-top: 1px solid var(--border);\n            padding: 12px 0;'
)

# 2. Hero slider text adjustments
content = content.replace('letter-spacing: 4px;', 'letter-spacing: 2px;')

# 3. Explore arrows desktop visibility
content = content.replace(
    '''        .explore-arrow {
            position: absolute;
            top: 50%;
            transform: translateY(-60%);
            width: 30px; height: 30px;
            border-radius: 50%;
            background: #e2e2e2;
            display: none;''',
    '''        .explore-arrow {
            position: absolute;
            top: 50%;
            transform: translateY(-60%);
            width: 30px; height: 30px;
            border-radius: 50%;
            background: #e2e2e2;
            display: flex;'''
)

# 4. Product grid adjustments (left align text, smaller text)
content = content.replace(
    '''        .product-title {
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 10px;
            line-height: 1.05;
            letter-spacing: .3px;
        }
        .product-price {
            font-size: 15px;
            font-weight: 700;
            margin: 2px 0 8px;
        }''',
    '''        .product-title {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            margin-top: 12px;
            line-height: 1.3;
            letter-spacing: 0.5px;
            text-align: left;
        }
        .product-price {
            font-size: 12px;
            font-weight: 700;
            margin: 4px 0 12px;
            text-align: left;
        }'''
)

# 5. Footer tweaks (smaller headings, tighter lines)
content = content.replace('text-transform: uppercase;\n            letter-spacing: 1px;\n            line-height: 1.1;', 'text-transform: uppercase;\n            letter-spacing: 1px;\n            line-height: 1.1;\n            font-size: 14px;')

with open('page.html', 'w') as f:
    f.write(content)

print("Fonts and styling updated successfully.")
