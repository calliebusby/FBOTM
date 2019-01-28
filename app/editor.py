from PIL import Image, ImageDraw, ImageFont
from app import data_manager
import urllib
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

    draw = ImageDraw.Draw(image)
    # TODO: text border
    # TODO: the width of the page and line break
    meme_font = ImageFont.truetype("Impact.ttf", 12)
    font_shadow = ImageFont.truetype("Impact.ttf", 12)
    (x, y) = (1, 1)
    color = 'rgb(255, 255, 255)'
    shadow_black = 'rgb(0, 0, 0)'

    draw.text((x - 2, y - 2), quote, (0, 0, 0), font=meme_font)
    draw.text((x + 2, y - 2), quote, (0, 0, 0), font=meme_font)
    draw.text((x + 2, y + 2), quote, (0, 0, 0), font=meme_font)
    draw.text((x - 2, y + 2), quote, (0, 0, 0), font=meme_font)
    draw.text((x, y), quote, fill=color, font=meme_font)
    image.save('finished_product.jpeg')
    return True


def select_image(the_boi):
    url = data_manager.find_daily_image(the_boi)
    print(url)
    return url
