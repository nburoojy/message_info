"""
  Get information about urls.

  Makes requests to the urls in parallel, then serially parses and searches for
  a title attribute. If one doesn't exist, returns no title. 

  This is a potentially DANGEROUS module and should NOT be used in production.

  Known issues:
  * This has potential to expose sensitive information on local networks. It
    should be deployed in an isolated environment without outbound access to
    non-public services.
  * This can be used to DDOS a third party site by sending a large amount of
    traffic.
  * It cannot find the title of web pages with robots.txt or ua filters.
  * An attacker could easily DDOS this service by requesting pages with long
    timeouts or large response sizes. The long timeouts would exhaust the
    thread pool and the large responses would exhaust memory.
  * It doesn't respect cache control headers, so it may send more traffic than
    the site can support.
  * The requests are parallel, but the parsing of the content is serial. With
    large responses, the parsing may be a performance bottleneck and could be
    improved with 1) cacheing urls 2) streaming content and stopping when the
    title is discovered 3) use parallelization to avoid the 1 cpu bottleneck.
"""
from lxml import html as lxml_html
import html
import grequests


TIMEOUT=5.0

def get_title(url, http_response):
  result = { 'url': url }
  if http_response and http_response.content:
    html_string = http_response.content
    tree = lxml_html.fromstring(html_string)
    title = tree.find(".//title").text
    if title:
      result['title'] = html.escape(title)

  return result

def get_titles(urls):
  requests = (grequests.get(u) for u in urls)
  responses = grequests.map(requests, gtimeout=TIMEOUT)
  
  return [get_title(url, response) for url, response in zip(urls, responses)]
