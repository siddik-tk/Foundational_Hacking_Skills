import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_url(url):
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(pattern, url) is not None


def is_valid_phone(phone):
    pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
    return re.match(pattern, phone) is not None


print(is_valid_phone("+919876543210"))
print(is_valid_phone("09876543210"))
print(is_valid_phone("1234567890"))
print(is_valid_url("https://google.com"))
print(is_valid_url("ftp://notvalid.com"))

print(is_valid_email("hacker@example.com"))
print(is_valid_email("hacker@bad_email"))
