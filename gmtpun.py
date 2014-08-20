#! /usr/bin/env python

from bottle import Bottle
from bottle import run
from bottle import request
from bottle import response
from bottle import static_file, template
from urlparse import urlparse, parse_qs
import os

GmtPun = Bottle()

@GmtPun.get('/')
def index_get(data=None):
  return static_file('index.html', root='.')

@GmtPun.post('/')
def index_post():
    import time
    time.sleep(5)

    inputarea = request.forms.get('search_result')
    print inputarea

    if inputarea:
        try:
            query = urlparse(inputarea).query
            params = parse_qs(query)
            result_url = params['url'][0]
        except:
            return None

        result_path = urlparse(result_url).path
        result_filename = os.path.basename(result_path)

        return template('result',
                        original_link = inputarea,
                        result_url=result_url,
                        result_filename=result_filename)
    else:
        return None

@GmtPun.route('/css/<css_file>')
def serve_css(css_file):
  return static_file(css_file, root='./css')

@GmtPun.route('/images/<filepath:path>')
def serve_images(filepath):
  return static_file(filepath, root='./images')

@GmtPun.route('/favicon.ico')
def serve_favicon():
  return static_file('favicon.ico', root='.')

@GmtPun.route('/js/<filepath:path>')
def serve_js(filepath):
  return static_file(filepath, root='./js')

# @GmtPun.route('/hello')
# def hello_again():
#     if request.get_cookie("visited"):
#         return "Welcome back! Nice to see you again"
#     else:
#         response.set_cookie("visited", "yes")
#         return "Hello there! Nice to meet you"

# @GmtPun.post('/')
# def form_submit():
#     inputarea = request.forms.get('search_result')
#     return "<p>You pipoo: %s</p>" %inputarea

if __name__ == '__main__':
    run(GmtPun,host='gmtpun.org', port=8080, debug=True,reloader=True)
