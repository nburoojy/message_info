"""
  Regular expression matching patterns.
  Used for identifying patterns in messages, for example, emoticons and
  mentions.
"""
import re


# Matches 'custom' emoticons which are alphanumeric strings, no longer than 15
# characters, contained in parenthesis. You can assume that anything matching
# this format is an emoticon. (https://www.hipchat.com/emoticons)
EMOTICON_REGEX = re.compile('\(([a-zA-Z0-9]{1,15})\)')

# Mentions start with an '@' and ends when hitting a non-word character.
MENTION_REGEX = re.compile('@(\w+)')

def find_emoticons(message):
  return EMOTICON_REGEX.findall(message)

def find_mentions(message):
  return MENTION_REGEX.findall(message)

