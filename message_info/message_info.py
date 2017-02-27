import re
import requests
from flask import Flask, jsonify, request
from .parser import link_parser, regex_parser
from .scraper import scraper

app = Flask(__name__)

@app.route('/', methods=['POST'])
def parse():
  message = request.values['message']

  response = {}
  mentions = regex_parser.find_mentions(message)
  emoticons = regex_parser.find_emoticons(message)
  links = scraper.get_titles(link_parser.find_links(message))
  
  if mentions:
    response['mentions'] = mentions

  if emoticons:
    response['emoticons'] = emoticons

  if links:
    response['links'] = links

  return jsonify(response)

if __name__ == "__main__":
  app.run()
