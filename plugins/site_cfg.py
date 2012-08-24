import os
import json

def preBuild(site):
    """
    Get site specific dictionary.
    """
    global site_cfg

    site_cfg = json.load(open(os.path.join(site.path, 'site.json'), 'r'))


def preBuildPage(site, page, context, data):
    context.update(site_cfg)
    return context, data