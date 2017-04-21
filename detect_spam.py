# -*- coding: utf-8 -*- 

# Spam detector
# License: CC0 1.0

from google.appengine.api import memcache

# https://cloud.google.com/appengine/docs/python/refdocs/google.appengine.api.memcache
def detect_spam(ip, interval = 600, count = 600):
  if not memcache.get(ip, namespace = 'spam') is None:
    return True
  key = ip + ' '
  value = memcache.incr(key, namespace = 'spam')
  if value is None:
    memcache.set(key, 0, time = interval, namespace = 'spam')
  elif int(value) >= count:
    memcache.set(ip, '', time = 24 * 60 * 60, namespace = 'spam')
  return False
