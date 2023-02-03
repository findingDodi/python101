import io

url_text = "Eine URL: https://www.example.com Noch eine URL:http://example.com KEINE url: http:/example.com auch KEINE url: ww.examole.com Dritte URL: {www.example.com}"

gefundene_urls = []
HTTP = "http://"
HTTPS = "https://"
WWW = "www."


def urls_finden(_gefundene_urls, _url_text):
    counter = 0
    while (_url_text != -1):
        counter += 1

    return 0


anzahl_gefundene_urls = urls_finden(gefundene_urls, url_text)
print(anzahl_gefundene_urls)
print(gefundene_urls)
