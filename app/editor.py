from PIL import Image, ImageDraw, ImageFont
from app import data_manager
import requests
from io import BytesIO


def append_quote(quote, the_boi):
    url = select_image(the_boi)
    r = requests.get(url)

    image = Image.open(BytesIO(r.content))

    # image = Image.open('the_boi.png')
    draw = ImageDraw.Draw(image)
    meme_font = ImageFont.truetype("Impact.ttf", 12)
    (x, y) = (50, 50)
    color = 'rgb(255, 255, 255)'

    draw.text((x, y), quote, fill=color, font=meme_font)
    image.save('finished_product.png')
    return True


def select_image(the_boi):
    url = data_manager.find_daily_image(the_boi)
    print(url)
    return url
