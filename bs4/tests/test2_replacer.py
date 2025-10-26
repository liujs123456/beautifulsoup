import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

html = "<b>Hello</b> <i>World</i>"
replacer = SoupReplacer("i", "em")

soup = BeautifulSoup(html, "html.parser", replacer=replacer)
print(soup.prettify())
