import urllib2
def download (reference):
    resp=urllib2.urlopen(reference)
    page=unicode(resp.read(), 'utf-8')
    splitPage=page.split('\n')
    return splitPage

if __name__ == '__main__':
  import codecs
  b_file = "4.htm"
  url = 'http://www.mosgortrans.ru/rasp/1/2188303/45140/3689/index.html'
  b_page = download(url)
  with codecs.open(b_file, encoding='utf-8') as f:
      for line1,line2 in zip(f,b_page):
          if line1.strip() != line2.strip():
                 print line1, line2
                 #print line1,line2
