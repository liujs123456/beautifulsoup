import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import sys
from bs4 import BeautifulSoup, SoupStrainer

def main():
    if len(sys.argv) < 2:
        print("How to run: python task4.py <input path>")
        return

    input_path = sys.argv[1]

    f = open(input_path, "r", encoding="utf-8")
    xml = f.read()
    f.close()

    only_id = SoupStrainer(attrs={"id": True})

    if input_path.endswith(".xml"):
        soup = BeautifulSoup(xml, "lxml-xml", parse_only=only_id)


    tags_with_id = soup.find_all(attrs={"id": True})

    if not tags_with_id:
        print("No tags with 'id' attribute found in the document.")
        return

    for tag in tags_with_id:
        print(f"<{tag.name}> id='{tag.get('id')}'")

    print("Total tags with id:", len(tags_with_id))

if __name__ == "__main__":
    main()
