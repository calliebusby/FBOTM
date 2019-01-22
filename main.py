import requests
from app import quote


def main():
    get_some_pictures('Xiumin')
    print(quote.get_todays_quote())


def get_some_pictures(the_boi):
    google_search = 'https://www.googleapis.com/customsearch/v1'

    search_params = {}
    search_params['q'] = the_boi
    search_params['key'] = 'AIzaSyDuoDdWZUbSL8CEcjdePYvhXjEuVzXdEt0'
    search_params['cx'] = '008071172635476624347:9zfhracf2vo'
    search_params['searchType'] = 'image'
    search_params['fileType'] = 'png'
    search_params['filter'] = '1'
    search_params['num'] = '10'

    r = requests.get(google_search, params=search_params)
    json_data = r.json()
    for item in json_data['items']:
        verify_link_not_broken(item['link'])


def verify_link_not_broken(link):
    try:
        r = requests.get(link)
        if r.status_code == requests.codes.ok:
            print(link)
    except:
        print("Ouch a link is dead")


def download_image(link):
    pass


def add_some_text():
    pass


if __name__ == '__main__':
    main()
