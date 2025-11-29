import sys
import os
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def main():
    if len(sys.argv) < 3:
        print("Usage: PYTHONPATH=. python apps/m2/task6.py apps/m2/sample.html apps/m2/sample_out.html")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    output_task6 = os.path.dirname(output_path)
    if output_task6 and not os.path.exists(output_task6):
        os.makedirs(output_task6)
        print(f"Created output folder: {output_task6}")

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            html = f.read()
        print("File read using UTF-8 ")
    except FileNotFoundError:
        print(f"Error! File Not Found: {input_path}")
        return

    replacer = SoupReplacer("b", "blockquote")

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    pretty_html = soup.prettify()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pretty_html)

    print(f" Replacement done during parsing")
    print(f" Output XML successfully created: {output_path}")


if __name__ == "__main__":
    main()