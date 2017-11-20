from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib 
import re

library_url = raw_input("library url please: ")
domain = raw_input("domain please: ")

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'src':
                if attr[1].find(domain) == -1:
                    if attr[1][0:1] != '/':
                        print("tag: " + tag)
                        print("src: " + str(attr))
                        
page = urllib.urlopen(library_url)

g = open('./test.tmp','w')
g.write(page.read())
g.close()

parser = MyHTMLParser()
f = open('./test.tmp','r')
parser.feed(f.read())
f.close()
h = open('./test.tmp','r')
print("Starting Grepper")
regex = r"src ?= ?\"(.*)?\""
for thing in re.findall(regex, h.read()):
    if thing.find(domain) == -1:
        if thing[1] == '/' or thing[0] != '/':
            print(thing)
