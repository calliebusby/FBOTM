import requests


def get_some_pictures(the_boi):
    google_search = 'https://www.googleapis.com/customsearch/v1'

    search_params = {}
    search_params['q'] = the_boi
    search_params['key'] = 'AIzaSyDuoDdWZUbSL8CEcjdePYvhXjEuVzXdEt0'
    search_params['cx'] = '008071172635476624347:9zfhracf2vo'
    search_params['searchType'] = 'image'
    search_params['fileType'] = 'jpeg'
    search_params['filter'] = '1'
    search_params['num'] = '10'

    valid_links = []
    for i in range(1, 61, 10):
        search_params['start'] = str(i)

        r = requests.get(google_search, params=search_params)
        json_data = r.json()
        for item in json_data['items']:
            link = verify_link_not_broken(item['link'])
            valid_links.append(link) if link is not None else None

    return valid_links


def verify_link_not_broken(link):
    try:
        r = requests.get(link)
        if r.status_code == requests.codes.ok:
            return link
    except:
        print("Ouch link is dead!")
