import re
import html

CLEANR = re.compile('<.*?>')

def sanitize_html(raw_html):
	cleantext = re.sub(CLEANR, '', raw_html)
	return html.unescape(cleantext)

