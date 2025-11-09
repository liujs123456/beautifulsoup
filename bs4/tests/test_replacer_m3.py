from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def rename_b_to_strong(tag):

    if getattr(tag, "name", None) == "b":
        return "strong"
    return tag.name

def drop_class_attr(tag):

    new_attrs = {}
    for k, v in tag.attrs.items():
        if k != "class":
            new_attrs[k] = v
    return new_attrs

def add_data_safe_yes(tag):
    tag.attrs["data-safe"] = "yes"

def rename_h1_to_h2(tag):
    if getattr(tag, "name", None) == "h1":
        return "h2"
    return tag.name

def attrs_cleaner_if_has_class(tag):
    if "class" in tag.attrs:
        return {"title": "new"}
    return tag.attrs

def add_meta_ok(tag):
    tag.attrs["data-meta"] = "ok"


def test_name_xformer_basic():
    html = "<div><b>Hello</b></div>"
    replacer = SoupReplacer(name_xformer=rename_b_to_strong)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "<strong>" in str(soup) and "</strong>" in str(soup)

def test_attrs_xformer_removes_class():
    html = '<p class="text" id="x">Hi</p>'
    replacer = SoupReplacer(attrs_xformer=drop_class_attr)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "class" not in str(soup)

def test_xformer_adds_data_attr():
    html = "<span>Text</span>"
    replacer = SoupReplacer(xformer=add_data_safe_yes)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "data-safe" in str(soup)

def test_combined_transformers():
    html = '<h1 class="a">Title</h1>'
    replacer = SoupReplacer(
        name_xformer=rename_h1_to_h2,
        attrs_xformer=attrs_cleaner_if_has_class,
        xformer=add_meta_ok,
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    s = str(soup)
    assert "<h2" in s
    assert 'title="new"' in s
    assert "data-meta" in s

def test_backward_compatibility_old_api():
    html = "<b>Hi</b>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "<blockquote>" in str(soup)

def test_replacer_safety_on_invalid_tag():
    html = "<div><b>ok</b></div>"
    def bad_xformer(tag):
        raise Exception("fail")
    replacer = SoupReplacer(xformer=bad_xformer)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "div" in str(soup)
