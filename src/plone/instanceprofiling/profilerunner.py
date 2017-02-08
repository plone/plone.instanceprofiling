import requests
import json
import time


CONTENT_URLS_URL = 'http://localhost:8080/Plone/@@content_urls'


def profilerunner():

    content_urls = requests.get(CONTENT_URLS_URL)
    content_urls = json.loads(content_urls.text)

    times_c = []
    times_t = []

    for cnt, url in enumerate(content_urls['content_urls']):

        server_times = requests.get(url + '/content_time')
        server_times = json.loads(server_times.text)

        times_c.append(server_times['clock'])
        times_t.append(server_times['real'])

        print("Current run {0}, clock {1}, time {2}".format(cnt, server_times['clock'], server_times['real']))

    c_rq_tot = sum(times_c)
    c_rq_min = min(times_c)
    c_rq_max = max(times_c)
    c_rq_avg = c_rq_tot / (cnt + 1)
    c_rq_med = sorted(times_c)[int(round(len(times_c) / 2))]

    t_rq_tot = sum(times_t)
    t_rq_min = min(times_t)
    t_rq_max = max(times_t)
    t_rq_avg = t_rq_tot / (cnt + 1)
    t_rq_med = sorted(times_t)[int(round(len(times_t) / 2))]

    print("Real time:")
    print("Minimum request time: {0}s {1}/s".format(t_rq_min, 1 / t_rq_min))
    print("Maximum request time: {0}s {1}/s".format(t_rq_max, 1 / t_rq_max))
    print("Average request time: {0}s {1}/s".format(t_rq_avg, 1 / t_rq_avg))
    print("Median request time: {0}s {1}/s".format(t_rq_med, 1 / t_rq_med))
    print("Total running time: {0}s".format(t_rq_tot))
    print
    print("CPU Time:")
    print("Minimum request time: {0}s {1}/s".format(c_rq_min, 1 / c_rq_min))
    print("Maximum request time: {0}s {1}/s".format(c_rq_max, 1 / c_rq_max))
    print("Average request time: {0}s {1}/s".format(c_rq_avg, 1 / c_rq_avg))
    print("Median request time: {0}s {1}/s".format(c_rq_med, 1 / c_rq_med))
    print("Total running time: {0}s".format(c_rq_tot))


if __name__ == '__main__':
    profilerunner()
