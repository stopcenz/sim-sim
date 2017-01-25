#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Wepbroxy for announce requests
# License: CC0 1.0

from detect_spam import *
import webapp2
import logging
import urllib
from google.appengine.api import urlfetch

# Параметры автоматической защиты от спама.

SPAM_DETECTOR_INTERVAL = 600 # анализируемый период времени в секундах
SPAM_DETECTOR_COUNT    = 1200 # максимально допустимое количество запросов для одного ip

class MainHandler(webapp2.RequestHandler):
  def get(self):
    if detect_spam(self.request.remote_addr, SPAM_DETECTOR_INTERVAL, SPAM_DETECTOR_COUNT):
      self.response.status_int = 403
      logging.warning('Spam')
      return
    
    url = self.request.path_qs[1:]
    if not '&ip=' in url and not '?ip=' in url:
      url += '&ip=' + urllib.quote(self.request.remote_addr)
      
    headers = {'Cache-Control': 'no-cache'}
    if self.request.user_agent:
      headers['User-Agent'] = self.request.user_agent
    
    try:
      result = urlfetch.fetch(url = url, headers = headers)
    except Exception as e:
      self.response.status_int = 504
      self.response.write(str(e))
      logging.error(str(e))
      return
      
    if result.status_code == 200:
      self.response.headers = result.headers
      self.response.write(result.content)
    else:
      if status_code < 512:
        self.response.status_int = result.status_code
      else: # fix unofficial codes
        self.response.status_int = 503
      logging.error(result.content)
      
app = webapp2.WSGIApplication([
    ('/.*', MainHandler)
], debug=False)

