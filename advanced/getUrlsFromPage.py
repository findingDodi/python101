import requests
from bs4 import BeautifulSoup


def sanitize_url(url, urli):
    if urli.startswith('/') or urli.startswith('#'):
        urli = '{}{}'.format(url, urli)
        urli.replace('//', '/')
        urli.replace('/#', '#')

    return urli


def get_urls_from_page(page_url):
    reqs = requests.get(page_url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    counter = 1
    print('Here are your urlis! :')

    for link in soup.find_all('a'):
        current_href = str(link.get('href'))
        current_urli = sanitize_url(page_url, current_href)

        if not current_urli:
            continue

        print(str(counter).ljust(5, ' '), current_urli)
        counter += 1


user_page_url = input('please enter page you like to get urlis from: ')
get_urls_from_page(user_page_url)
