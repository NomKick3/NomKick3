from PIL import Image, ImageDraw

# Ladda in bild (byt ut input.png mot namnet på .png-filen med din bild)
input_image = Image.open("Utter.png")
input_pixels = input_image.load()

# Skapa resultatbild
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Beräkna pixlarnas RGB-värden och placera bildpunkterna
for x in range(output_image.width):
    for y in range(output_image.height):
        r, g, b, a = input_pixels[x, y]
        temp = g
        r = b
        g = r
        b = temp
        draw.point((x, y), (r, g, b, a))

output_image.save("output.png")