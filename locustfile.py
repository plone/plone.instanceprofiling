from locust import HttpLocust
from locust import task
from locust import TaskSet
from pyquery import PyQuery
from BeautifulSoup import BeautifulSoup

import json
import random
import requests

CONTENT_URLS_URL = 'http://localhost:8080/Plone/@@content_urls'


class WebsiteTasks(TaskSet):

    def _load_resources(self, resources, attr):
        for it in resources:
            url = it.attrib[attr]
            if "localhost" in url:
                self.client.get(url)
                print url

    def _load_content_urls(self):
        ret = requests.get(CONTENT_URLS_URL)
        return json.loads(ret.text)['content_urls']

    def on_start(self):
        self.content_urls = self._load_content_urls()

    @task
    def index(self):
        url = random.choice(self.content_urls)
        # url = "/"

        ret = self.client.get(url)

        # That shit doesn't work. pq('html') doesn't find anything.
        # Using BeautifulSoup's prettifier doesn't help either.

        # html = BeautifulSoup(ret.content)
        # pq = PyQuery(html.prettify())

        # css = pq('link[rel="stylesheet"]')
        # self._load_resources(css, 'href')

        # js = pq('script')
        # self._load_resources(js, 'src')

        # imgs = pq('img')
        # self._load_resources(imgs, 'src')


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
    host = 'http://localhost:8080/Plone'
