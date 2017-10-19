import urlparse
import urllib2
import os
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print "[*] Please download and install Beautiful Soup first!"
    sys.exit(0)

url = raw_input("[+] Enter the url: ")
download_path = raw_input("[+] Enter the download path in full: ")

try:
    headers - {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}

    i = 0

    request = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html.read())

    for tag in soup.findAll('a', href=True):
       tag['href'] = urlparse.urljoin(url, tag['href'])

    if os.path.splitext(os.path.basename(tag['href']))[1] == '.jpg':
       current = urllib2.urlopen(tag['href'])
       print "\n[*] Downloading: %s" %(os.path.basename(tag['href']))

       f = open(download_path + "\\" +os.path.basename(tag['href'], "wb"))
       f.write(current.read())
       f.close()
       i+=1

    print "\n[*] Downloaded %d files" %(i+1)
    raw_input("[+] Press any key to exit...")

except KeyboardInterrupt:
    print "[*] Exiting..."
    sys.exit(1)

except URLError as e:
    print "[*] Could not get information from server!!"
    sys.exit(2)

except:
    print "I don't know the problem but sorry!!"
    sys.exit(3)
