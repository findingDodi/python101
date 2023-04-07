import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

content_array = []
base_url = 'https://swapi.dev/api/people/?page='
counter = 1
keep_running = True

while keep_running:
    print(counter)
    try:
        url = base_url + str(counter)
        url_response = urllib.request.urlopen(url)
        url_response_status = url_response.status

        if url_response_status != 200:
            keep_running = False

        url_content = url_response.read().decode()
        content_array.append(url_content)

    except Exception as ex:
        # print(ex)
        keep_running = False

    counter += 1

for i in range(len(content_array)):
    # print(content_array[i])
    decoded = json.loads(content_array[i])
    # print(decoded["results"])
    results = decoded["results"]
    for result in results:
        print(result['name'])
