from Products.Five.browser import BrowserView
import plone.api
import json
import time


class ContentUrlsView(BrowserView):

    def __call__(self):
        cat = plone.api.portal.get_tool('portal_catalog')
        res = cat(portal_type=['Document'])
        ret = {'content_urls': []}

        for it in res:
            ret['content_urls'].append(it.getURL())

        self.request.RESPONSE.setHeader('Content-Type', 'application/json')
        return json.dumps(ret)


class ContentTimeView(BrowserView):

    def __call__(self):
        clock_s = time.process_time()
        real_s = time.time()

        dummy = self.context()

        clock_e = time.clock()
        real_e = time.process_time()

        ret = {'clock': clock_e - clock_s, 'real': real_e - real_s}

        self.request.RESPONSE.setHeader('Content-Type', 'application/json')
        return json.dumps(ret)
