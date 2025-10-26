import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import sys
import time
from bs4 import BeautifulSoup, SoupStrainer

def main():
    if len(sys.argv) < 2:
        print("How to run: python task2.py <input path>")
        return

    input_path = sys.argv[1]

    start = time.time()
    f = open(input_path, "r", encoding="utf-8")
    xml = f.read()
    f.close()

    only_a = SoupStrainer("a")
    if input_path.endswith(".xml"):
        soup = BeautifulSoup(xml, "lxml-xml", parse_only=only_a)

    links = soup.find_all("a")
    for a in links:
        href = a.get("href")
        text = a.get_text()
        print("Text:", text)
        print("URL:", href)

    cost = time.time() - start

    print("Total links found:", len(links))
    print("Runtime:", cost, "seconds")

if __name__ == "__main__":
    main()
