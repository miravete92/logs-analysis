# "Database code" for the DB Forum.

import datetime
import psycopg2

DBNAME = 'news'

def get_most_popular():
  """Return the most popular news."""
  conn = psycopg2.connect(database=DBNAME)
  c = conn.cursor()
  c.execute("select count(log.id) as views, title from articles join log on path like '%' || slug || '%' where status='200 OK' and method='GET' group by articles.id order by views desc limit 3 ;")
  return c.fetchall()
  conn.close()

def get_popular_authors():
  """Return the most popular authors."""
  conn = psycopg2.connect(database=DBNAME)
  c = conn.cursor()
  c.execute("select count(log.id) as views, authors.name as author from articles join log on path like '%' || slug || '%' join authors on authors.id = articles.author where status='200 OK' and method='GET' group by authors.id order by views desc")
  return c.fetchall()
  conn.close()
  
def get_error_days():
  """Returns which days did more than 1% of requests lead to errors."""
  conn = psycopg2.connect(database=DBNAME)
  c = conn.cursor()
  c.execute("select round(sub.perc,1) as perc, to_char(sub.day,'Mon DD, YYYY') as day from (select date_trunc('day', time) as day, sum(case when status<>'200 OK' then 1 else 0 end) * 100.0 / count(*) as perc from log group by day) sub where perc > 1")
  return c.fetchall()
  conn.close()


