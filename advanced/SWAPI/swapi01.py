import urllib.request
import http.client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

http_response: http.client.HTTPResponse = urllib.request.urlopen('https://swapi.dev/api/people/')
print(http_response.status)

content_array = []
base_url = 'https://swapi.dev/api/people/?page='
counter = 1
keep_running = True

while keep_running:
    try:
        url = base_url + str(counter)
        url_response = urllib.request.urlopen(url)
        url_response_status = url_response.status

        if url_response_status != 200:
            keep_running = False

        url_content = url_response.read()
        content_array.append(url_content)

    except Exception as ex:
        print(ex)
        keep_running = False

    counter += 1

for i in range(len(content_array)):
    print(content_array[i])
