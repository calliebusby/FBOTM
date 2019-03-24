from app import data_manager
from app import editor
from PIL import Image, ImageDraw, ImageFont


def main():
    quote_of_the_day = 'Fuckface, the real winners in life are the people who look at every situation with an expectation that they can make it work or make it better'
    image = Image.open('./test_images/bruce-dickinson_web.jpg')

    editor.outline_text(image, quote_of_the_day, 4, 4)
    # outline_text(image, quote_of_the_day, 1, 1)
    image.save('Bruce_meme.jpg')


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


if __name__ == '__main__':
    main()
