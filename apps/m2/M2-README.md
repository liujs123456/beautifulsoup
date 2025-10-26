# Milestone-2 Part-2:


| API Function | Source File | Line Number | Usage Purpose |
|-------------|-------------|------------:|---------------|
| `BeautifulSoup()` | bs4/__init__.py |         133 | Create parser for HTML/XML input |
| `find_all()` | bs4/element.py |        2715 | Search matching tags |
| `get_text()` | bs4/element.py |         524 | Extract text content |
| `get()` | bs4/element.py |        2160 | Read attribute value |
| `prettify()` | bs4/formatter.py |        2601 | Output formatted HTML |
| `SoupStrainer` | bs4/filter.py |         313 | Filter nodes for faster parsing |
---

## Milestone-2 Part-3: 

### API Overview
SoupReplacer allows replacing one HTML tag with another throughout parsing.
For example:
```html
<i>Hello</i>  →  <em>Hello</em>
```
### How to run task6
cd ~/Desktop/beautifulsoup<br>
source .venv/bin/activate<br>
python apps/m2/task6.py apps/m2/Text.xml apps/m2/output_task6.xml<br>

#### If everything is correct, you will get a new file called output_task6.




