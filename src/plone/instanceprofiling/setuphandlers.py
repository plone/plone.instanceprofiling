# -*- coding: utf-8 -*-
from zope.component.hooks import getSite
from collective.contentcreator import create_item_runner


def post_install(context):
    """Post install script"""
    portal = getSite()

    portal.portal_setup.runAllImportStepsFromProfile(
        'plone.app.contenttypes:default'
    )

    content_structure = []
    for cnt in range(400):
        content_structure.append(
            {
                "type": "Document",
                "title": "Document " + str(cnt),
                "data": {
                    "description": "Some thing."
                }
            }
        )

    create_item_runner(
        getSite(),
        content_structure,
        default_lang='en',
        default_wf_action='publish'
    )
