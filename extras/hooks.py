import os
import re

def preBuild(path, config):
    import re
    import render
    import shutil
    import codecs
    from datetime import datetime, date
    import markdown

    from cactus import Config
    site_cfg = Config(os.path.join(path, 'site.json'))
    print site_cfg._data

    src_dir = os.path.join(path, 'posts')
    dst_dir = os.path.join(path, 'pages/posts')

    # Make the ouput directory
    shutil.rmtree(path=dst_dir, ignore_errors=True)
    os.mkdir(dst_dir)

    # Convert all the markdown files in the src directory to HTML and put
    # the new pages in the dst directory.
    md = markdown.Markdown(extensions = ['meta', 'codehilite'])

    def toPostFilename(m):
        return m.group(2) + '.html'

    test = re.compile(r'^(\d{4}-\d{2}-\d{2})-([a-z\-]+)\.markdown')
    files = [(os.path.join(src_dir, f), os.path.join(dst_dir, test.sub(toPostFilename, f))) for f in os.listdir(src_dir) if test.search(f)]

    posts = []
    for (infile, outfile) in files:

        print "  * Converting %s" % infile

        if not os.path.exists(outfile):

            # Read in markdown and convert it to HTML
            f = codecs.open(infile)
            source = f.read()
            f.close()

            html = md.convert(source)

            # Write out new article as HTML
            f = codecs.open(outfile, 'w', 'utf8')

            title = md.Meta['title'][0].encode('utf-8')
            post_date = datetime.strptime(md.Meta['date'][0], "%Y/%m/%d %H:%M:%S")

            f.write('{% extends "article.html" %}\n')
            f.write('{%% block title %%}%s{%% endblock %%}\n' % title)
            f.write('{%% block content %%}\n<h1>%s</h1>\n<p class="postdate">Posted %s</p><br/>%s\n{%% endblock %%}\n' % (title, post_date.strftime("%B %d, %Y"), html))
            f.close()

            # Add the post to our list of posts to be used later for building
            # the site archive or latest pages listing.
            page = os.path.relpath(outfile, os.path.join(path, 'pages'))

            posts.append((post_date,       # For sorting
                                {
                                    "datetime": post_date,
                                    "title": title,
                                    "author": md.Meta['authors'][0].encode('utf-8'),
                                    "page": page,
                                    "permalink": '/'.join([site_cfg.get('SITE_URL'), page]),
                                    "content": html
                                 }))
        else:
            print "ERROR: Multiple files with same title: %s" % title
            print "       Continuing on anyway."

    # Now build a chronological list of posts and their information for a template
    # to use.  The order is newest to oldest.
    render.global_context["POST_LISTING"] = [post[1] for post in sorted(posts, reverse=True)]
    render.global_context.update(site_cfg._data)

def postBuild(path, config):
    import shutil
    shutil.rmtree(path=os.path.join(path, 'pages/posts'), ignore_errors=True)

def preDeploy(path, config):

    # Add a deploy log at /versions.txt

    import urllib2
    import datetime
    import platform
    import codecs
    import getpass

    url = config.get('aws-bucket-website')
    data = u''

    try:
        data = urllib2.urlopen('http://%s/versions.txt' % url).read() + u'\n'
    except:
        pass

    data += u'	'.join([datetime.datetime.now().isoformat(), platform.node(), getpass.getuser()])
    codecs.open(os.path.join(path, 'build', 'versions.txt'), 'w', 'utf8').write(data)

def postDeploy(path, config):
    pass
