# -*- coding: utf-8 -*-
from zope.component.hooks import getSite
from collective.loremipsum.utils import create_subobjects


def post_install(context):
    """Post install script"""
    portal = getSite()
	import pdb; pdb.set_trace()
    create_subobjects(
        portal,
        portal,
        {
           'portal_type': ['Page', 'News Item', 'Event'],
           'amount': 100,
           'recurse': True,
           'recursion_depth': 3,
           'recurse_same_ptypes': True,
           'publish': True,
        }
    )
