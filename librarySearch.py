from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'src':
                print("tag: " + tag)
                print("src: " + str(attr))

parser = MyHTMLParser()
f = open('./UmbLibrary','r')
parser.feed(f.read())
