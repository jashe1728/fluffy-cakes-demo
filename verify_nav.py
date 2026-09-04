from html.parser import HTMLParser
from pathlib import Path

PAGES = ["index.html", "menu.html", "about.html", "gallery.html", "contact.html"]
EXPECTED = ["Home", "Menu", "Our story", "Gallery"]

class NavParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.depth = 0
        self.links = []
        self.html = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav" and attrs.get("id") == "site-menu":
            self.inside = True
            self.depth = 1
        elif self.inside:
            self.depth += 1
        if self.inside:
            self.html.append(self.get_starttag_text())
        if self.inside and tag == "a" and self.depth == 2:
            self.links.append("")

    def handle_endtag(self, tag):
        if self.inside:
            self.html.append(f"</{tag}>")
            self.depth -= 1
            if tag == "nav" and self.depth == 0:
                self.inside = False

    def handle_data(self, data):
        if self.inside:
            self.html.append(data)
            if self.links and self.depth == 2:
                self.links[-1] += data

for page in PAGES:
    parser = NavParser()
    parser.feed(Path(page).read_text(encoding="utf-8"))
    assert parser.links == EXPECTED, (page, parser.links)
    nav_html = "".join(parser.html)
    assert "There is something special" not in nav_html, page
    assert "Há algo de especial" not in nav_html, page

js = Path("site.js").read_text(encoding="utf-8")
assert "document.querySelectorAll('#site-menu > a')" in js
assert "body:not([data-page]) nav a" not in js
print("PASS: 5 pages expose exactly 4 clean primary nav links")
print("PASS: translation targets only #site-menu > a; no broad fallback selector")
