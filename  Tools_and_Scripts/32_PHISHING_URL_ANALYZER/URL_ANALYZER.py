import re
from urllib.parse import urlparse

shorteners = ['bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly', 'is.gd']
ip_regex = re.compile(r'\bhttp[s]?://\d{1,3}(?:\.\d{1,3}){3}\b')

def is_suspicious(url):
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    if ip_regex.match(url):
        return "IP-based URLs are suspicious [x]"
    elif any(short in netloc for short in shorteners):
        return "Shortened URL are very suspicious [x]"
    elif "-" in netloc or netloc.count('.') >= 3:
        return "Suspicious no of domains [!]"
    else:
        return "Looks Safe [-]"

def scan_urls(file_path):
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    for url in urls:
        result = is_suspicious(url)
        print(f"[*] {url} → {result}")

scan_urls("urls.txt")