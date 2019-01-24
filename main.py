from app import editor
from app import image_retriever
from app import quote


def main():
    image_retriever.get_some_pictures('Xiumin')
    quote_of_the_day = quote.get_todays_quote()
    print(quote_of_the_day)

    editor.append_quote(quote_of_the_day)


def download_image(link):
    pass


if __name__ == '__main__':
    main()
