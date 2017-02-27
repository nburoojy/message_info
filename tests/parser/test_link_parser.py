"""
    Tests the URL parser. 
"""

import pytest
from message_info.parser import link_parser


def test_find_links():
    """Test finding links in messages."""
    assert [] == link_parser.find_links('simple')
    assert ['http://simple.com'] == link_parser.find_links('http://simple.com')

    # If unusual punctuation comes in the uri path, it's considered part of the url
    # Unusual punctuation is not captured as part of the TLDN
    # This could cause unexpected results if ending a sentence or parenthetical
    # remark with a url immediately followed with punctuation.
    assert ['http://simple.com'] == link_parser.find_links('Check out this link! http://simple.com')
    assert ['http://simple.com'] == link_parser.find_links('Check out this link http://simple.com!')
    assert ['http://simple.com/!'] == link_parser.find_links('Check out this link http://simple.com/!')
    assert ['http://simple.com'] == link_parser.find_links('Check out this link http://simple.com.')
    assert ['http://simple.com/.'] == link_parser.find_links('Check out this link http://simple.com/.')
    assert ['http://simple.com'] == link_parser.find_links('Check out this link (http://simple.com)')
    assert (['https://en.wikipedia.org/wiki/Disambiguation_(disambiguation)'] ==
        link_parser.find_links('Check out https://en.wikipedia.org/wiki/Disambiguation_(disambiguation)'))
    # The user may expect "https://en.wikipedia.org/wiki/)" -- the article on the left paren
    assert (['https://en.wikipedia.org/wiki/))'] ==
        link_parser.find_links('Check out (https://en.wikipedia.org/wiki/))'))
    assert ['https://simple.com'] == link_parser.find_links('https://simple.com')
    assert ['https://sim.ple.com'] == link_parser.find_links('https://sim.ple.com')
    assert [] == link_parser.find_links('ftp://sim.ple.com')
    assert ['http://a.com', 'http://b.com'] == link_parser.find_links('http://a.com http://b.com')
