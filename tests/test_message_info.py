"""
    Tests the message info scraper. 
"""

import pytest
from message_info import message_info
from unittest.mock import patch


@patch('message_info.parser.regex_parser.find_emoticons')
@patch('message_info.parser.regex_parser.find_mentions')
def test_parse_message(find_mentions, find_emoticons):
    """Test finding entities in messages."""
    find_mentions.return_value = ['nick']
    find_emoticons.return_value = ['happy']
    assert {'mentions': ['nick'], 'emoticons': ['happy']} == message_info.parse_message('message')

@patch('message_info.scraper.scraper.get_titles')
@patch('message_info.parser.link_parser.find_links')
def test_parse_message_links(find_links, get_titles):
    """Test finding entities in messages."""
    find_links.return_value = ['http://nick.com', 'http://example.com']
    get_titles.return_value = [{'url': 'http://nick.com', 'title': 'Nick'}, {'url': 'http://example.com'}]
    assert {'links': [
        {'url': 'http://nick.com', 'title': 'Nick'},
	{'url': 'http://example.com'}]} == message_info.parse_message('message')
