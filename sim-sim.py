# -*- coding: utf-8 -*- 

# Sim-Sim 
# Version 6
# GAE-based proxy server

# Author: stopcenz - stopcenz@gmail.com
# License: CC0 1.0

"""
Автор передает этот код в общественное достояние путём отказа от всех своих прав 
на эту компьютерую программу по всему миру, включая все связанные и смежные права, 
которые он имеет по отношению к данной программе, в той степени, в которой 
это допускается законом.

Вы можете копировать, изменять, распространять этот код, даже в коммерческих целях,
не спрашивая разрешения. 

Автор не даёт никаких гарантий относительно программы и не несет ответственности 
за все виды использования, в максимально возможной степени, допустимой 
применяемым правом.
"""

##########################################################################################
#                                       Настройки
##########################################################################################
#
# Ограничение доступа:
# 1 - могут зайти только администраторы сайта (рекомендуется)
# 0 - нет ограничений
# Редактировать список администраторов можно в консоли Goggle Cloud:
# https://console.cloud.google.com/iam-admin/iam/
# Будьте осторожны. Администраторы смогут изменять многие настройки вашего сайта.

ADMINS_ONLY = 1

# Максимальный размер (в байтах) для документов HTML, XML или CSS внутри которых
# ссылки автоматически преобразуются. Более длинные будут переданы как есть.
# Допустимы значения от 0 (неограниченно) до 33554432.
# Учтите, обработка больших документов потребует много времени и памяти,
# кроме того, документы больше 32Мб в любом случае вызовут ошибку сервера.

MAX_LENGHT_HTML = 2000000 

# Удаляемые из ответа сервера заголовки. Указываются в нижнем регистре.

SKIPPED_HEADERS = [
  "content-encoding",
  "content-security-policy", 
  "transfer-encoding",
  "x-content-security-policy", 
  "content-security-policy-report-only", 
  "x-content-security-policy-report-only",
  "x-webkit-csp",
  "x-webkit-csp-report-only",
  "public-key-pins", 
  "public-key-pins-report-only"]
  
# Длина токена (часть доменного имени, указанной длины, перед символами "-dot-").

TOKEN_LENGTH = 5

# Блокируемые токены.
# Если вы по каким-либо причинам хотите заблокировать отдельный токен впишите его в список.
# Входящие запросы в которых встречаются указанные токены будут перенаправлены на главную.
# Например:
# BLOCKED_TOKENS = ["abcde", "fgh012"]

BLOCKED_TOKENS = []

# Параметры автоматической защиты от спама.

SPAM_DETECTOR_INTERVAL = 600  # анализируемый период времени в секундах
SPAM_DETECTOR_COUNT    = 1200 # максимально допустимое количество запросов для одного ip

# Перечисленные сайты открываются напрямую минуя прокси

ECXCLUDED_HOSTS = [
  "appspot.com",
  "googlevideo.com",
  "youtube.com",
  "youtu.be",
  "ytimg.com",
  "vimeo.com",
  "vimeocdn.com",
  "googleapis.com",
  "bootstrapcdn.com",
  "onion",
  "lib",
  "i2p",
  "local"]

# Если видео потребляет много трафика можно отключить его передачу (1)

DISABLE_VIDEO_CONTENT = 0

# Примеры заблокированных доменов для показа на главной

SAMPLE_HOSTS = ["kinozal.tv", "lib.rus.ec", "ej.ru"]

# Время (в секундах) ожидания ответа удаленного сервера

URLFETCH_DEADLINE = 50

##########################################################################################

NUMERALS = '0123456789abcdefghijklmnopqrstuvwxyz'

from detect_spam import *
from home_page import *
from site_patches import *

import datetime
import logging
import random
import re
import time
import urllib
import webapp2

from google.appengine.api import memcache
from google.appengine.api import urlfetch
from google.appengine.api import users

#https://webapp2.readthedocs.io/en/latest/
class MainHandler(webapp2.RequestHandler):
  def get(self):    self.any()
  def head(self):   self.any()
  def put(self):    self.any()
  def patch(self):  self.any()
  def delete(self): self.any()
  def post(self):
    self.root_host = str(self.request.host.split('-dot-', 1)[-1])
    if self.request.host != self.root_host:
      self.any()
      return
    
    if not ADMINS_ONLY and \
       detect_spam(self.request.remote_addr, SPAM_DETECTOR_INTERVAL, SPAM_DETECTOR_COUNT):
      logging.warning('Spam')
      return
    if ADMINS_ONLY and not users.IsCurrentUserAdmin():
      return
    
    if not 'url' in self.request.POST or \
       len(self.request.POST['url']) < 4 or \
       not 'token' in self.request.POST or \
       not self.is_valid_token(self.request.POST['token']):
      logging.error('Broken init post:\r\n' + self.request.body[:999])
      logging.error('\r\n'.join(['%s: %s' % (k, v) for (k, v) in self.request.headers.items()]))
      self.redirect('https://' + self.root_host)
      return
    
    token = self.request.POST['token']
    url = self.request.POST['url']
    if not re.search(r'^(http:\/\/|https:\/\/)', url, flags = re.IGNORECASE):
      url = 'http://' + url
    
# Fix non-latin url: https://ru.wikipedia.org/wiki/Левковские
    percent_encoded_url = ''
    for c in url:
      if ord(c) < 127:
        percent_encoded_url += c
      else:
        percent_encoded_url += urllib.quote(c.encode('utf-8'))
    self.redirect(str(self.encode_url(percent_encoded_url, token)))


  def any(self):
    if not ADMINS_ONLY and \
       detect_spam(self.request.remote_addr, SPAM_DETECTOR_INTERVAL, SPAM_DETECTOR_COUNT):
      # If you think adding captcha here is a good idea
      self.response.status_int = 403
      logging.warning('Spam')
      return
    
    if '/robots.txt' == self.request.path:
      self.show_robots_txt()
      return
    
    self.root_host = str(self.request.host.split('-dot-', 1)[-1])
    if self.request.host == self.root_host:
      self.show_home_page()
      return
      
    (scheme, host, port, token) = self.unpack_host()
    if scheme is None:
      self.redirect(str('https://' + self.root_host))
      return
    
    (scheme, host, path_qs) = patch_host_back(scheme, host, self.clean_path_qs)
    url = scheme + '://' + host
    if port:
      if scheme == 'https':
        if port != '443':
          url += ':' + port
      elif port != '80':
        url += ':' + port
    
    url += path_qs
    logging.debug(url)
    
    if token in BLOCKED_TOKENS:
      self.redirect(str('https://' + self.root_host))
      logging.info('Blocked token')
      return
    if not self.is_stored_token(token):
      self.redirect(str('https://' + self.root_host + '/' + url), code = 307)
      return
    
# https://cloud.google.com/appengine/docs/python/refdocs/modules/google/appengine/api/urlfetch
    try:
      result = urlfetch.fetch(
        url              = url,
        payload          = self.request.body,
        method           = self.request.method,
        headers          = self.get_modified_request_headers(scheme, host, port),
        allow_truncated  = False,
        follow_redirects = False,
        deadline         = URLFETCH_DEADLINE)
    except Exception as e:
      self.response.status_int = 504
      self.response.write('<h1>Error</h1><p>' + str(e))
      logging.error(str(e))
      return
      
    content = result.content
    self.response.headers = {}
    
    for header_line in result.header_msg.headers:
      (name, value) = header_line.split(':', 1)
      value = value.strip(' \r\n')
      name_l = name.lower()
      if name_l in SKIPPED_HEADERS:
        continue
      if 'set-cookie' == name_l:
        match = re.match(r'(^.+;\s*Domain=\.?)([^ ;]+)(.*$)', value, flags = re.IGNORECASE)
        if match:
          if match.group(2).lower() != host:
            continue
          else:
            value = match.group(1) + self.request.host + match.group(3)
      if 'location' == name_l:
        value = self.encode_url(value, token, scheme, mode = 'header')
      if 'content-type' == name_l:
        if DISABLE_VIDEO_CONTENT and value.lower().startswith('video/'):
          self.response.status_int = 404
          return
        content = self.modify_content(content, value, scheme, host, token)
      self.response.headers.add_header(name, value)
    
    if result.status_code < 512: # fix cloudflare codes
      self.response.status_int = result.status_code
    else:
      self.response.status_int = 504
    
    self.response.write(content)


  def modify_content(self, content, content_type_value, scheme, host, token):
    if MAX_LENGHT_HTML < 1 or len(content) <= MAX_LENGHT_HTML:
      content_type = re.split('[:; \/\\\\=]+', content_type_value.lower())
      if len(content_type) > 1 and content_type[0] in ['text', 'application']:
        if content_type[1] in ['html', 'xml', 'xhtml+xml', 'plain']:
          content = patch_html(scheme, host, self.request.path, content)
          content = self.encode_url(content, token, scheme, mode = 'html')
        elif content_type[1] in ['css']:
          content = patch_css(scheme, host, self.request.path, content)
          content = self.encode_url(content, token, scheme, mode = 'css')
        elif content_type[1] in ['javascript']:
          content = patch_js(scheme, host, self.request.path, content)
        elif content_type[1] in ['bittorrent', 'x-bittorrent']:
          content = patch_torrent(scheme, host, self.request.path, content, self.root_host)
    return content


# site-com-3token-dot-app-id.appspot.com -> ('http', 'site.com', '', 'token')
# sub-domain-site-com-8080-93token-dot-app-id.appspot.com -> ('http', 'sub-domain.site.com', '8080', 'token')
  def unpack_host(self):
    regexp = r'^([-a-z0-9]+-[a-z]{2,9})(-{1,2})([0-9]{1,5}-|)([a-z0-9]+)([a-z0-9]{' 
    regexp += str(TOKEN_LENGTH) + r'})-dot-'
    match = re.match(regexp, self.request.host)
    if match is None:
      return (None, None, None, None)
    port = match.group(3)[:-1]
    host_name_list = list(match.group(1))
    pos = -1
    for num36 in match.group(4):
      pos += NUMERALS.index(num36) + 2
      if pos >= len(host_name_list) or host_name_list[pos] != '-':
        return (None, None, None, None)
      host_name_list[pos] = '.'
    if len(match.group(2)) > 1:
      scheme = 'https'
    else:
      scheme = 'http'
    token = match.group(5)
    return (scheme, ''.join(host_name_list), port, token)


  def get_modified_request_headers(self, scheme, host, port):
    def dashrepl(matchobj):
      if matchobj.group(1):
        result = scheme + '://' + host
        if port:
          result += ':' + port
        return scheme + '://' + host
      return host
    regexp = r'(https:\/\/|)' + re.escape(self.request.host)
    result = {}
    for name, value in self.request.headers.iteritems():
      name_l = name.lower()
      if not name_l.startswith('x-') and name_l != 'referer':
        result[name] = re.sub(regexp, dashrepl, value, flags = re.IGNORECASE)
    return result

 
  def encode_url(self, text, token, current_scheme = 'http', mode = None):
    def dashrepl(matchobj):
      host = matchobj.group(4).strip('.').lower()
      if self.is_exluded_host(host) or '-dot-' in host:
        return matchobj.group(0)
      scheme = matchobj.group(3).lower()
      if '//' == scheme:
        scheme = current_scheme
      port = matchobj.group(5)[1:]
      path = matchobj.group(6)
      (scheme, host, path) = patch_host(scheme, host, path)
      
      dot_pos = ''
      for l in map(lambda s: len(s), host.split('.')[:-1]):
        if l < 1 or l > len(NUMERALS):
          return matchobj.group(0)
        dot_pos += NUMERALS[l - 1]
      result = matchobj.group(1) + 'https://' + host.replace('.', '-') + '-' 
      
      if scheme.startswith('https'):
        result += '-'
        if port != '' and port != '443':
          result += port + '-'
      elif port != '' and port != '80':
      	result += port + '-'
      	
      result += dot_pos + token + '-dot-' + self.root_host + path
      return result 
    
    if mode == 'css':
      regexp = r'((url)\s*\(\s*[\'"]?)(https?:|)\/\/'
    elif mode == 'html':
      regexp = r'(\<[^\<\>]+\s(src|href|action)=[\'"]?)(https?:|)\/\/'
    elif mode == 'header':
      regexp = r'((^))(https?:|)\/\/'
    else:
      regexp = r'(())(https?:|^)\/\/'
    regexp += r'([a-z0-9][-a-z0-9\.]*\.[a-z]{2,9})\.?(:[0-9]{1,5}|)(\/[-_\.~%\/a-z0-9]+|)'
    return re.sub(regexp, dashrepl, text, flags = re.IGNORECASE)


  def is_exluded_host(self, host):
    for exluded_host in ECXCLUDED_HOSTS:
      if host == exluded_host or host.endswith('.' + exluded_host):
        return True
    return False


  def show_robots_txt(self):
    self.response.headers = {'Content-Type': 'text/plain'}
    if '-dot-' in self.request.host:
      self.response.write('User-agent: *\r\nDisallow: /')
    else:
      self.response.write('User-agent: *\r\nAllow: /')


  def show_home_page(self):
    self.response.headers = {
      'Content-Type': 'text/html; charset=utf-8',
      'Strict-Transport-Security': 'max-age=31536000; preload'}
    if ADMINS_ONLY and not users.IsCurrentUserAdmin():
      if users.get_current_user():
        self.response.status_int = 403
        self.response.write('<h1>Forbidden</h1>')
      else:
        self.redirect(str(users.create_login_url(self.request.path_qs)))
      return
    
    url = self.request.path_qs[1:]
    token = self.get_token_from_cookie()
    if not token:
      token = self.get_new_token()
    else:
      if len(url) > 11 and re.search(r'^https?:\/\/', url.lower()):
        self.redirect(str(self.encode_url(url, token)), code = 307)
        return
    
    if len(url) < 5:
      url = random.choice(SAMPLE_HOSTS or [''])
    content = home_page.replace('%%host%%', self.root_host)
    content = content.replace('%%url%%', url)
    content = content.replace('%%token%%', token)
    content = content.replace('%%year%%', str(datetime.datetime.now().year))
    self.response.write(content)
    
    
  def get_new_token(self):
    while True:
      token = ''.join(random.choice(NUMERALS) for _ in range(TOKEN_LENGTH))
      if not token in BLOCKED_TOKENS and memcache.get(token, namespace = 'tokens') is None:
        break
    memcache.set(token, [self.request.remote_addr], 60 * 60, namespace = 'tokens')
    self.response.set_cookie(
      'token',
      token,
      path      = '/', 
      domain    = self.request.host, 
      secure    = True, 
      httponly  = True, 
      overwrite = True,
      expires   = datetime.datetime(2038, 1, 1))
    return token


  def get_token_from_cookie(self):
    if 'token' in self.request.cookies:
      token = self.request.cookies['token']
      if self.is_valid_token(token):
        value = memcache.get(token, namespace = 'tokens') or []
        if not self.request.remote_addr in value:
          value.append(self.request.remote_addr)
        memcache.set(token, value, 60 * 60, namespace = 'tokens')
        return token
    return None


  def is_valid_token(self, token):
    return re.search(r'^[a-z0-9]{' + str(TOKEN_LENGTH) + r'}$', token)


  def is_stored_token(self, token):
    value = memcache.get(token, namespace = 'tokens')
    if value is None or not self.request.remote_addr in value: 
      return False
    memcache.set(token, value, 60 * 60, namespace = 'tokens')
    return True
  
  
  @property
  def clean_path_qs(self):
    # preventing modify path_qs in webapp2.RequestHandler
    qs = self.request.environ.get('QUERY_STRING')
    if qs:
      return self.request.environ['PATH_INFO'] + '?' + qs
    
    return self.request.environ['PATH_INFO']
      
  
app = webapp2.WSGIApplication([
  ('/.*', MainHandler)
], debug=False)
