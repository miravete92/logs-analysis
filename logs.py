from logsdb import get_most_popular, get_popular_authors, get_error_days
import time

def showReport():
  '''Main page of the log.'''
  print '\nCurrent log analysis report at %s' % time.strftime("%c")
  print '=========================================================='
  
  print '\nMost viewed news'
  print '----------------'  
  
  print "".join('"%s" - %s views\n' % (views, title) for title, views in get_most_popular())

  print '\nTop authors by views'
  print '--------------------'
  print "".join('%s - %s views\n' % (views, author) for author, views in get_popular_authors())
  
  print '\nDaily error rate > 1%'
  print '--------------------'
  print "".join('%s - %s %% errors\n' % (perc, day) for day, perc in get_error_days())

showReport()

