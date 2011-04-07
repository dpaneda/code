
import urllib
import xml.etree.ElementTree as ET # Python 2.5
# import elementtree.ElementTree as ET

def RSS(tag): return "{http://purl.org/rss/1.0/}" + tag
def DC(tag): return "{http://purl.org/dc/elements/1.1/}" + tag

class Post(object):
    def __init__(self, item):
        self.link = item.findtext(RSS("link"))
        self.title = item.findtext(RSS("title"))
        self.description = item.findtext(RSS("description"))
        self.pubdate = item.findtext(DC("date"))
        self.tags = item.findtext(DC("subject"), "").split()

def getposts(user, tag=""):
    if isinstance(tag, tuple):
        tag = "+".join(tag)
    uri = "http://del.icio.us/rss/%s/%s" % (user, tag)
    tree = ET.parse(urllib.urlopen(uri))
    return map(Post, tree.getiterator(RSS("item")))

for post in getposts("sark79"):
    print post.link, post.tags
