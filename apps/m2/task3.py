import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import sys
from bs4 import BeautifulSoup, SoupStrainer

def main():
    if len(sys.argv) < 2:
        print("How to run: python task3.py <input path>")
        return

    input_path = sys.argv[1]

    f = open(input_path, "r", encoding="utf-8")
    xml = f.read()
    f.close()

    only_tags = SoupStrainer(True)
    if input_path.endswith(".xml"):
        soup = BeautifulSoup(xml, "lxml-xml", parse_only=only_tags)


    all_tags = soup.find_all(True)
    if not all_tags:
        print("No tags found in the document.")
        return

    for tag in all_tags:
        print(f"<{tag.name}>")

    print("Total tags found:", len(all_tags))

if __name__ == "__main__":
    main()
