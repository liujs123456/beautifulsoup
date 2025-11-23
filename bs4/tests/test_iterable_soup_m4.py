from bs4 import BeautifulSoup

def _pick_markers(soup):
    wanted_tags = ["div", "b", "span"]
    wanted_texts = ["t1", "t2", "t3"]
    result = []
    for n in soup:
        if hasattr(n, "name") and n.name in wanted_tags:
            result.append("<" + n.name + ">")
        else:
            s = str(n).strip()
            if s in wanted_texts:
                result.append(s)
    return result


def test_preorder():
    html = "<div>t1<b>t2</b><span>t3</span></div>"
    soup = BeautifulSoup(html, "html.parser")

    got = _pick_markers(soup)
    want = ["<div>", "t1", "<b>", "t2", "<span>", "t3"]

    assert got == want


def test_text():
    html = "<div>t1<b>t2</b><span>t3</span></div>"
    soup = BeautifulSoup(html, "html.parser")

    texts = []
    for n in soup:
        s = str(n).strip()
        if s and getattr(n, "name", None) is None:
            texts.append(s)

    assert "t1" in texts
    assert "t2" in texts
    assert "t3" in texts


def test_empty():
    soup = BeautifulSoup("", "html.parser")
    items = []
    for n in soup:
        items.append(n)
    assert items == []


def test_break():
    html = "<div>t1<b>t2</b><span>t3</span></div>"
    soup = BeautifulSoup(html, "html.parser")

    count = 0
    for _ in soup:
        count += 1
        if count == 3:
            break

    assert count == 3


def test_deep_structure():
    html = "<div>"
    i = 0
    while i < 30:
        html += "<span>"
        i += 1
    html += "X"
    i = 0
    while i < 30:
        html += "</span>"
        i += 1
    html += "</div>"

    soup = BeautifulSoup(html, "html.parser")

    count = 0
    for _ in soup:
        count += 1
        if count == 5:
            break

    assert count == 5

#pytest bs4/tests/test_iterable_soup_m4.py -v