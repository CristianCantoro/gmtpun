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
def index_get():
  return static_file('index.html', root='public_html')

@GmtPun.post('/')
@GmtPun.post('/gmtpun/')
def index_post():
    inputarea = request.forms.get('search_result')

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


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description='Test GMTPUN locally.')
    parser.add_argument('-d', dest='debug', action='store_true',
                       help='Debug mode.')
    parser.add_argument('--host', dest='host', default='localhost',
                       help='Hostname to use (default: localhost).')
    parser.add_argument('-p', dest='port', default=8888,
                       help='Port number to use (default: 8888).')
    parser.add_argument('-r', dest='reloader', action='store_false',
                       help='Disable reloader mode.')

    args = parser.parse_args()
    args.port = int(args.port)

    # When testing locally, let Bottle handle static files
    @GmtPun.route('/static/<resource>/<filepath:path>')
    def serve_static(resource, filepath):
      return static_file(filepath,
                         root='./public_html/static/{}'.format(resource))

    @GmtPun.route('/favicon.ico')
    def serve_favicon():
      return static_file('favicon.ico', root='./public_html/')

    run(GmtPun, host=args.host,
                port=args.port,
                debug=args.debug,
                reloader=args.reloader)
