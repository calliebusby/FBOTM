from PIL import Image, ImageDraw, ImageFont


def append_quote(quote):
    image = Image.open('./test_images/grafi.jpg')
    draw = ImageDraw.Draw(image)
    meme_font = ImageFont.truetype("Impact.ttf", 52)
    (x, y) = (50, 50)
    color = 'rgb(255, 255, 255)'

    draw.text((x, y), quote, fill=color, font=meme_font)
    image.save('finished_product.jpg')
