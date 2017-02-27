
# Message Info Service

## Intro

This is a simple message info service. It receives chat messages and returns information about specific elements in the message.
It currently supports identifying mentions (for example "@user"), custom emoticons ("I'm (happy)"), and URLs.
For URLs, it attempts to discover the title of the page. If it can't find the title, only the URL is returned.

## Libraries

I chose the Flask python microframework because it's relatively simple to get started. I haven't used Flask before, but it was simpler to get started with than, for example, Django.

I use grequests to make asynchronous http request for resolving link titles. Also, I use lxml for parsing the title from html.
Finally, I use @dperini URL parsing regex because the acceptable URL format is very complex and this is already a (mostly) solved problem. There are still some edge cases with punctuation at the end of a URL that could cause unexpected results, and if I had more time, I would like to explore solutions.

## Set up
__Build__
```
xcode-select --install
sudo pip install virtualenv
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
pip install --editable .
```
__Run__
`FLASK_APP=message_info flask run`

To use the service, post a form with a field named `message` to the / route.
Since the input format wasn't fully specified, I chose to use a field in a form rather than using the entire content to store the message. I made this choice to allow for more flexibility in the future. There will likely be other fields associated with the request, for example a requestId could be propagated alongside all requests through each microservice involved in the top-level event. Then the microservice logs could be stitched together in an offline process and the developer could have a more coherent view into a single request's lifecycle.
`http -f post 127.0.0.1:5000/ message="test mention @foo"`

### Test
`pip install pytest`
`py.test tests/`

## Todo

If I had more time to work on this, I would make these improvements.

* Move url lookups into a service. More details about this issue are [here](https://github.com/nburoojy/message_info/blob/master/message_info/scraper/scraper.py)
* Implement url caching
* Implement url and domain throttling (avoid DDOSing 3rd parties)
* Improve title performance: by streaming responses and html parsing
* Prevent massive url response attack
* Evaluate the attack vectors. For example, large or malformed inputs may lead to security or reliability issues.
* Improve URL parsing.
  * How to resolve "google.com" (without http) to a URL
  * How to solve the punctuation at the end of the URL issue (as [tested](https://github.com/nburoojy/message_info/blob/master/tests/parser/test_link_parser.py#L26))
* Monitoring: At a minimum, I would want metrics about requests/second, error rates, response latency, CPU and memory usage.
* Alerting on those metrics
* I've been able to trigger an issue that looks like [this](https://github.com/kennethreitz/requests/issues/3752) with python 3.6 via the grequests library.
* Logging
