import re
number_barcodes = int(input())

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for _ in range(number_barcodes):
    product_group = '00'
    barcode = input()
    match = re.match(pattern, barcode)
    if match:
        digits = re.finditer(r"\d", barcode)
        digits = [digit.group() for digit in digits]
        if digits:
            product_group = ''.join(digits)
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')