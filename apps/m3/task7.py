import sys
from pathlib import Path
from bs4 import BeautifulSoup

def main():
    # Extract the command line parameters, input is parameter 1, output is parameter 2
    if len(sys.argv) < 3:
        print("How to run: PYTHONPATH=. python apps/m3/task7.py apps/m3/Text.xml apps/m3/Text_out.xml")
        return

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    try:
        html = input_path.read_text(encoding="utf-8")
        print("File has been read with UTF-8.")
    except FileNotFoundError:
        print("File Not Found: {input_path}")
        return

    # Initialize the BeautifulSoup object
    if str(input_path).lower().endswith(".xml"):
        soup = BeautifulSoup(html, "lxml-xml")
    else:
        soup = BeautifulSoup(html, "lxml")

    # ============= task7 =============
    p_tags = soup.find_all("p")
    changed = 0
    for p in p_tags:
        p["class"] = "test"
        changed += 1

    pretty_html = soup.prettify()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pretty_html)

    print(f"Updated {changed} <p> tag(s).")
    print(f"Written to: {output_path.resolve()}")

if __name__ == "__main__":
    main()
