from bs4 import BeautifulSoup
from bs4.element import NavigableString

html = "<div>t1<b>t2</b><span>t3</span></div>"
soup = BeautifulSoup(html, "html.parser")

for n in soup:
    if isinstance(n, NavigableString):
        s = str(n).strip()
        if s:
            print("TEXT", s)
    else:
        print("TAG", n.name)

#PYTHONPATH=. python apps/m4/demo.py