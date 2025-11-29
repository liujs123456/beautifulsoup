import sys
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def set_p_class(tag):
    if getattr(tag, "name", None) == "p":
        tag.attrs["class"] = "test"

def main():
    if len(sys.argv) < 3:
        print("How to run: PYTHONPATH=. python apps/m3/task7.py apps/m3/Text.xml apps/m3/Text_out.xml")
        return

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    try:
        html = input_path.read_text(encoding="utf-8")
        print("File has been read with UTF-8.")
    except FileNotFoundError:
        print(f"File Not Found: {input_path}")
        return


    replacer = SoupReplacer(xformer=set_p_class)
    if str(input_path).lower().endswith(".xml"):
        soup = BeautifulSoup(html, "lxml-xml", replacer=replacer)
    else:
        soup = BeautifulSoup(html, "lxml", replacer=replacer)

    changed = sum(1 for _ in soup.find_all("p"))

    pretty_html = soup.prettify()
    output_path.write_text(pretty_html, encoding="utf-8")

    print(f"Updated {changed} <p> tag(s).")
    print(f"Written to: {output_path.resolve()}")

if __name__ == "__main__":
    main()