from html.parser import HTMLParser
from pathlib import Path
import re

path = Path('/root/fluffy-cakes-demo/index.html')
text = path.read_text()
assert path.exists() and path.stat().st_size > 10000
assert '<title>Fluffy Cakes' in text
assert 'assets/fluffy-cakes-logo-brown.png' in text
assert Path('/root/fluffy-cakes-demo/assets/fluffy-cakes-logo-brown.png').exists()
shared_js = Path('/root/fluffy-cakes-demo/site.js').read_text()
assert 'IntersectionObserver' in shared_js
assert 'localStorage' in shared_js and 'language-switcher' in text
assert 'prefers-reduced-motion' in text
assert text.count('data-reveal') >= 8
parser = HTMLParser()
parser.feed(text)
assert parser.get_starttag_text() is not None
scripts = re.findall(r'<script>(.*?)</script>', text, re.S)
Path('/tmp/fluffy-cakes-demo.js').write_text('\n'.join(scripts))
print('html_bytes=', path.stat().st_size)
print('script_blocks=', len(scripts))
print('reveal_hooks=', text.count('data-reveal'))
print('sections=', len(re.findall(r'<section(?: |>)', text)))
print('checks=passed')
