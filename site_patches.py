# site-specific corrections

import re

def patch_host(scheme, host, path):
  if host in ['dl.kinozal.tv', 'dl.kinozal.me']:
    # cookie visibility correction
    host = host[3:]
    path = '/.dl.' + path
  return (scheme, host, path)
  
  
def patch_host_back(scheme, host, path):
  if host in ['kinozal.tv', 'kinozal.me']:
    if path.startswith('/.dl./'):
      host = 'dl.' + host
      path = path[5:]
  return (scheme, host, path)
  

def patch_html(scheme, host, path, content):
  if host in ['rutracker.org', 'rutracker.net', 'rutracker.cr']:
    if path.endswith('.php'):
      # fix login
      srch = "cur_domain : location.hostname.replace(/.*?([^.]+\.[^.]+)$/, '$1'),"
      repl = "cur_domain : location.hostname,"
      content = content.replace(srch, repl, 1)
  return content


def patch_js(scheme, host, path, content):
  if host == 'static.t-ru.org':
     # fix login
    if path.endswith('.all.min.js'):
      srch = ';this.action=(a?"https:":"http:")+"//"'
      repl = ';this.action="https://"'
      content = content.replace(srch, repl, 1)
  return content


def patch_torrent(scheme, host, path, content, root_host):
  if host == 'dl.kinozal.tv':
    poxy_url = 'https://' + root_host + '/'
    def dashrepl(matchobj):
      length = int(matchobj.group(1)) + len(poxy_url)
      return str(length) + ':' + poxy_url + matchobj.group(2)
    regexp = r'([0-9]{2,3}):(http:\/\/tr[0-5]\.torrent4me\.com\/ann)'
    content = re.sub(regexp, dashrepl, content, count = 2)
  return content


def patch_css(scheme, host, path_qs, content):
  return content

