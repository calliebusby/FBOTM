from PIL import Image, ImageDraw, ImageFont
from app import data_manager
from io import BytesIO
from urllib.request import Request, urlopen


def append_quote(quote, the_boi):
    url = select_image(the_boi)

    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'})

    with urlopen(req) as f:
        b = BytesIO(f.read())
        image = Image.open(b)

    # TODO: the width of the page and line break
    outline_text(image, quote, 1, 1)

    image.save('finished_product.jpeg')
    return True


def select_image(the_boi):
    url = data_manager.find_daily_image(the_boi)
    print(url)
    return url


def outline_text(image, quote, x, y):
    draw = ImageDraw.Draw(image)
    font_size = calculate_font_size(image)
    meme_font = ImageFont.truetype("Impact.ttf", 12)
    white = 'rgb(255, 255, 255)'
    black = 'rgb(0, 0, 0)'
    draw.text((x - 2, y - 2), quote, black, font=meme_font)
    draw.text((x + 2, y - 2), quote, black, font=meme_font)
    draw.text((x + 2, y + 2), quote, black, font=meme_font)
    draw.text((x - 2, y + 2), quote, black, font=meme_font)
    draw.text((x, y), quote, fill=white, font=meme_font)


def calculate_font_size(image):
    return 10
