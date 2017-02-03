import requests
import json
import time


CONTENT_URLS_URL = 'http://localhost:8080/Plone/@@content_urls'


def profilerunner():

    import pdb
    pdb.set_trace()

    content_urls = requests.get(CONTENT_URLS_URL)
    content_urls = json.loads(content_urls.text)

    times = []

    for cnt, url in enumerate(content_urls['content_urls']):
        time_a = time.time()
        requests.get(url)
        time_b = time.time()
        times.append(time_b - time_a)
        print("Current run {0}, duration {1}".format(cnt, time_b - time_a))

    print("Minimum request time: {0}".format(min(times)))
    print("Maximum request time: {0}".format(max(times)))
    print("Average request time: {0}".format(sum(times) / (cnt + 1)))
    print("Total running time: {0}".format(sum(times)))
