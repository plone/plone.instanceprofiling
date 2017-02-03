from Products.Five.browser import BrowserView
import plone.api
import json


class ContentUrlsView(BrowserView):

    def __call__(self):
        cat = plone.api.portal.get_tool('portal_catalog')
        res = cat(portal_type=['Document'])
        ret = {'content_urls': []}

        for it in res:
            ret['content_urls'].append(it.getURL())

        self.request.RESPONSE.setHeader('Content-Type', 'application/json')
        return json.dumps(ret)
