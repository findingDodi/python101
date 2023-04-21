import urllib.request
import json
import ssl
import os.path
from ThePersonFactory import ThePersonFactory

ssl._create_default_https_context = ssl._create_unverified_context

content_array = []
base_url = 'https://swapi.dev/api/people/?page='
counter = 1
keep_running = True

while keep_running:
    file_name = 'content/swapi-people-{}.json'.format(counter)
    if not os.path.isfile(file_name):
        try:
            url = base_url + str(counter)
            url_response = urllib.request.urlopen(url)
            url_response_status = url_response.status

            if url_response_status != 200:
                keep_running = False

            url_content = url_response.read().decode()
            file_handle = open(file_name, "w")
            file_handle.write(url_content)
            file_handle.close()
            content_array.append(url_content)

        except Exception as ex:
            keep_running = False
    else:
        file_handle = open(file_name, "r")
        file_content = file_handle.read()
        file_handle.close()
        content_array.append(file_content)

    counter += 1

galaxy_people = []
for i in range(len(content_array)):
    decoded = json.loads(content_array[i])
    galaxy_people += ThePersonFactory.create_persons_from_data_list(decoded["results"])

counter = 0
for person in galaxy_people:
    counter += 1
    print('[{:02d}] {}'.format(counter, person))


