import requests
from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError
import json
import re
from urlparse import urlparse
from urlparse import urljoin
from pyquery import PyQuery as pq
"""
#get title, description, favicon, twitter card, facebook open graph data
def get_url_body(url):
    r = requests.get(url)
    status = r.status_code
    if status/100 == 2 or status/100 == 3:
        return r.text
    else:
        return ""
def parse_html(url):
    r = get_url_body(url)
    if r:
        d = pq(r)
        head = d("head")
        if head:
            d = pq(head)
            title = d("title")
            print title.text()


parse_html("http://www.nytimes.com/2014/04/11/books/francine-proses-lovers-at-the-chameleon-club-paris-1932.html?_r=0")


"""    
def parse_html(url):

  response = requests.get(url)
  data = {}
  data["title"] = ""
  data["description"] = None
  data["favicon"] = None
  data["facebook"] = {}
  data["twitter"] = {}

  try:
    if response.status_code/100 == 2 or response.status_code == 3: 
        soup = BeautifulSoup(response.text)

        #get title
        if soup.title.string:
          data["title"] = soup.title.string

        #get favicon
        parsed_uri = urlparse( url )
        if soup.find("link", rel="shortcut icon"):
          icon_rel = soup.find("link", rel="shortcut icon")["href"]
          icon_abs = urljoin( url, icon_rel )
          data["favicon"] = icon_abs
        else:
          domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
          data["favicon"] = domain + 'favicon.ico'

        #get description
        if soup.find('meta', attrs={'name':'description'}):
          data["description"] = soup.find('meta', attrs={'name':'description'})["content"]

        #get facebook open graph data
        if soup.findAll('meta', {"property":re.compile("^og")}):
          for tag in soup.findAll('meta', {"property":re.compile("^og")}):
            tag_type = tag['property']
            data["facebook"][tag_type] = tag['content']
            if tag_type == "og:description" and data["description"] is None:
              data["description"] = tag["content"]

        #get twitter card data
        if soup.findAll('meta', attrs={'name':re.compile("^twitter")}):
          for tag in soup.findAll('meta', attrs={'name':re.compile("^twitter")}):
            tag_type = tag['name']
            if 'content' in tag.attrs:
              data["twitter"][tag_type] = tag['content']
              if tag_type == "twitter:description" and data["description"] is None:
                data["description"] = tag["content"]

        print(json.dumps(data))

    else:
      print( "URL returned status %s" % response.code)

  except HTMLParseError:
    print ("Error parsing page data" )
"""
  handler.finish()
"""
parse_html("http://nyti.ms/1hH4xfK")
parse_html("http://wp.me/p2L7Ik-GCWh")

