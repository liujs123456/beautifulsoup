# Milestone 4 — Iterable BeautifulSoup 

## Goal
- Make `BeautifulSoup` (and any `Tag`) **iterable** → `for node in soup:`
- **Pre-order, left-to-right** traversal; yields both **Tag** and **NavigableString**
- **Lazy** streaming via `yield` (no full-list materialization)

## Usage
```python
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
```
**Expected(Pre-order）**
```
TAG div
TEXT t1
TAG b
TEXT t2
TAG span
TEXT t3
```

## Tests & Demo 
- Run tests 
  ```bash
  pytest bs4/tests/test_iterable_soup_m4.py -v
  ```
- demo 
  ```bash
  PYTHONPATH=. python apps/m4/demo.py
  ```
