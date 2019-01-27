from app import data_manager
from app import editor
from app import image_retriever
from app import quote


def main():
    the_boi = 'Xiumin'

    conn = data_manager.create_connection('FBOTD.db')
    data_manager.create_images_table(conn)
    data_created = data_manager.verify_data_created(conn, the_boi)

    if not data_created:
        image_arr = image_retriever.get_some_pictures(the_boi)
        data_manager.add_new_images_collection(conn, the_boi, image_arr)

    quote_of_the_day = quote.get_todays_quote()
    print(quote_of_the_day)

    editor.append_quote(quote_of_the_day, the_boi)


if __name__ == '__main__':
    main()
