"""
    Tests the url scraper.
"""

import pytest
from message_info.scraper import scraper
from unittest.mock import patch

class FakeHtml:
  def __init__(self, content):
    self.content = content

@patch('grequests.map')
@patch('grequests.get')
def test_parse_message(get_fn, map_fn):
    """Test finding entities in messages."""
    get_fn.return_value = []
    map_fn.return_value = [FakeHtml('<html><head><title>Nick</title></head></html>')]
    assert [{'url': 'foo.com', 'title': 'Nick'}] == scraper.get_titles(['foo.com'])

