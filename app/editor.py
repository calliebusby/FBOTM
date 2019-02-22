from PIL import Image, ImageDraw, ImageFont
from app import data_manager
from io import BytesIO
from urllib.request import Request, urlopen


def append_quote(quote, the_boi):
    quote = 'You must be the change you want to see in the world....'
    custom_quote = nickname_customizer(quote, the_boi)
    url = select_image(the_boi)

    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'})

    with urlopen(req) as f:
        b = BytesIO(f.read())
        image = Image.open(b)

    # TODO: the width of the page and line break
    # TODO: center text
    outline_text(image, custom_quote, 1, 1)

    image.save('finished_product.jpeg')
    return True


def nickname_customizer(quote, the_boi):
    nickname = data_manager.retrieve_nickname_from_db(the_boi)
    custom_quote = '%s, %s' %(nickname, quote)
    custom_quote = custom_quote.capitalize()
    return custom_quote


def select_image(the_boi):
    url = data_manager.find_daily_image(the_boi)
    print(url)
    return url


def outline_text(image, quote, x, y):
    draw = ImageDraw.Draw(image)
    font_size = calculate_font_size(draw, image, quote)
    meme_font = ImageFont.truetype("Impact.ttf", font_size)
    white = 'rgb(255, 255, 255)'
    black = 'rgb(0, 0, 0)'
    draw.text((x - 2, y - 2), quote, black, font=meme_font)
    draw.text((x + 2, y - 2), quote, black, font=meme_font)
    draw.text((x + 2, y + 2), quote, black, font=meme_font)
    draw.text((x - 2, y + 2), quote, black, font=meme_font)
    draw.text((x, y), quote, fill=white, font=meme_font)


def calculate_font_size(draw, image, quote):
    text_width, h = draw.textsize(quote, ImageFont.truetype("Impact.ttf"))

    image_width = image.width * 0.75
    font_size = 10
    while text_width < image_width:
        text_width, h = draw.textsize(quote, ImageFont.truetype("Impact.ttf", font_size))
        font_size += 2

    return font_size
