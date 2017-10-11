#HW6b
#Olivia Gardella

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
#    print(tag.get('href', None))

#count = int(input('Enter count: '))
counter = 0
#position = int(input('Enter position: '))
x = 0
url = 'http://py4e-data.dr-chuck.net/known_by_Giacomo.html'
while counter < 7:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')

    for i in tags:
        x = x + 1
        if x == 18:
            ad = i.get('href', None)

            x = 0
            break
    counter = counter + 1

print (ad)
