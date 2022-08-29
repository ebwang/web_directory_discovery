import requests

def request_http(url):
    print('Checking http://' + url)
    try:
        return requests.get("http://" + url, timeout=0.0010)
    except requests.exceptions.ConnectionError:
        pass

def request_https(url):
    print('Checking https://' + url)
    try:
        return requests.get("https://" + url, timeout=0.010)
    except requests.exceptions.ConnectionError:
        pass


targetURL = input("Enter Target URL: ")
file = open("common.txt", "r")
for line in file:
    line = line.strip('\n')
    fullURL = targetURL + "/" + line
    response_http = request_http(fullURL)
    response_https = request_https(fullURL)
    if (response_http or response_https):
        print('[+] Discovered Directory at Link: ' + fullURL)