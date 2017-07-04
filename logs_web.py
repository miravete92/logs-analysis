#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for
from logsdb import get_most_popular, get_popular_authors, get_error_days

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Logging</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>DB Logs</h1>
    <!-- post content will go here -->
    <h2>Article Views</h2>
    <ul>
%s
    </ul>
    <h2>Author Views</h2>
    <ul>
%s
    </ul>
    <h2>Days with error&gt;1%%</h2>
    <ul>
%s
    </ul>
  </body>
</html>
'''

# HTML template for an individual comment
VIEW = '''\
    <li>"%s" - %s views</li>
'''

AUTOR_VIEW = '''\
    <li>%s - %s views</li>
'''

ERROR = '''\
    <li>%s - %s %% errors</li>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the log.'''
    article_views = "".join(VIEW % (views, title) for title,
                            views in get_most_popular())

    author_views = "".join(AUTOR_VIEW % (views, author) for author,
                           views in get_popular_authors())

    log_errors = "".join(ERROR % (perc, day) for day,
                         perc in get_error_days())

    html = HTML_WRAP % (article_views, author_views, log_errors)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
