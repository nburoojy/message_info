"""
    Tests the MessageInfo regex parser.
"""

import pytest
from message_info.parser import regex_parser


def test_mentions():
    """Test mentions."""
    assert [] == regex_parser.find_mentions('simple')
    assert ['simple'] == regex_parser.find_mentions('@simple')
    assert [] == regex_parser.find_mentions('@')
    assert ['first', 'second'] == regex_parser.find_mentions('@first @second')
    assert ['first', 'second'] == regex_parser.find_mentions('@first@second')
    assert ['first', 'first'] == regex_parser.find_mentions('@first @first')
    assert ['is_A_word'] == regex_parser.find_mentions('@is_A_word-no')
    assert ([('long' * 100)] == regex_parser.find_mentions('@' + ('long' * 100)))

def test_emoticons():
    """Test emoticons."""
    assert [] == regex_parser.find_emoticons('simple')
    assert ['simple'] == regex_parser.find_emoticons('(simple)')
    assert ['simple'] == regex_parser.find_emoticons('abc(simple)123')
    assert [] == regex_parser.find_emoticons('()')
    assert ['Alpha123'] == regex_parser.find_emoticons('(Alpha123)')
    assert ['first', 'second'] == regex_parser.find_emoticons('(first) (second)')
    assert ['first', 'second'] == regex_parser.find_emoticons('(first)(second)')
    assert ['first', 'first'] == regex_parser.find_emoticons('(first) (first)')

    # Emoticons must be alphanumeric (not just 'words')
    assert [] == regex_parser.find_emoticons('(is_A_word)')
    assert [] == regex_parser.find_emoticons(')(')
    assert ['inner'] == regex_parser.find_emoticons('((inner))')
    assert ['inner', 'inner2'] == regex_parser.find_emoticons('(out(inner)(inner2)side)')

    # Emoticons can be at most 15 chars long
    assert ([('l' * 15)] == regex_parser.find_emoticons('(' + ('l' * 15) + ')'))
    assert ([] == regex_parser.find_emoticons('(' + ('l' * 16) + ')'))

