# init 
# (bytes) 8 bit = 1 kb
# resolution of 800 x 600 pixels
gif = 1
jpeg = 3
png = 3
tiff = 6
resolution = 800 * 600

# Assume 1 GB is 1,000,000,000 bytes
gb = 1000000000

size = int(input('Enter USB size (GB): '))

usbSize = size * gb

# Compression
gifSize = (gif * resolution) / 5
jpegSize = (jpeg * resolution) / 25
pngSize = (png * resolution) / 8
tiffSize = (tiff * resolution)

# Total
gifTotal = int(usbSize / gifSize)
jpegTotal = int(usbSize / jpegSize)
pngTotal = int(usbSize / pngSize)
tiffTotal = int(usbSize / tiffSize)

# Print results
print()
print(format(gifTotal, ','), 'GIF format images can be stored')
print(format(jpegTotal, ','), 'JPEG format images can be stored')
print(format(pngTotal, ','), 'PNG format images can be stored')
print(format(tiffTotal, ','), 'TIFF format images can be stored')
