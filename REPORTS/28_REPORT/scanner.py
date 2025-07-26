import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote
from datetime import datetime
import sys

payloads = [
    "' OR 1=1 --",
    "<script>alert(1)</script>",
    "\"><img src=x onerror=alert(1)>"
]


def get_all_forms(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "lxml")
        return soup.find_all("form")
    except Exception as e:
        print(f"[-] Error loading page: {e}")
        sys.exit(1)


def get_form_details(form):
    details = {}
    action = form.get("action") #form is an json or dictionary so we can use get()
    method = form.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.get("type", "text")
        input_name = input_tag.get("name")
        if input_name:
            inputs.append({"type": input_type, "name": input_name})

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submit_form(form_details, base_url, payload):
    target_url = urljoin(base_url, form_details["action"])

    data = {}
    for input_field in form_details["inputs"]:
        if input_field["type"] in ["text", "search", "email"]:
            data[input_field["name"]] = quote(payload)
        else:
            data[input_field["name"]] = "test"

    print(f"\n[+] Submitting payload to: {target_url}")
    print(f"[+] Data: {data}")

    try:
        if form_details["method"] == "post":
            response = requests.post(target_url, data=data, timeout=5)
        else:
            response = requests.get(target_url, params=data, timeout=5)
        return response
    except requests.exceptions.Timeout:    #XECE2545PTI544O232NN4245452435DJDJFJGHDF442342354BHFB
        print("[-] Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"[-] Request error: {e}")
    return None


def scan_for_vulnerable_forms(url):
    print(f"\nScanning Target: {url}")
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} form(s) on {url}\n")

    for i, form in enumerate(forms, start=1):
        form_details = get_form_details(form)

        for payload in payloads:
            print(f"Trying payload: {payload}")
            response = submit_form(form_details, url, payload)

            if response is None:
                continue

            content = response.text
            decoded_payload = payload.replace("<", "&lt;").replace(">", "&gt;")

            if payload in content or decoded_payload in content:
                print(f"    [!!!] Possible Vulnerability Detected!")
                print(f"         Payload: {payload}")
                print(f"         URL: {response.url}")
                log_result(url, form_details, payload, True)
                break
            else:
                print(f"    [-] Payload did not reflect.")

        print("-" * 50)


def log_result(url, form_details, payload, is_vulnerable):
    with open("scan_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} | {url}\n")
        log_file.write(f"Form: {form_details['action']}\n")
        log_file.write(f"Method: {form_details['method'].upper()}\n")
        log_file.write(f"Payload: {payload}\n")
        log_file.write(f"VULNERABLE: {'YES' if is_vulnerable else 'NO'}\n")
        log_file.write("=" * 60 + "\n")


if __name__ == "__main__":
    target = input("Enter URL to scan : ").strip()
    scan_for_vulnerable_forms(target)
