 Form Vulnerability Scanner (Basic Python Tool)

This is a simple Python script I built as part of my web app security learning. It 
scans for HTML forms in a target URL and tests them for basic SQL injection and
XSS vulnerabilities using predefined payloads.

The idea behind this is to understand how forms can be abused by attackers 
if proper input validation is missing.

What It Does

->Detects and extracts all forms from a given page
->Automatically fills input fields with test payloads
->Submits the form using GET/POST depending on the method
->Checks if the payload reflects back in the response
->Logs possible vulnerabilities with a timestamp

 Payloads Used

->`' OR 1=1 --` → basic SQL injection
->`<script>alert(1)</script>` → basic reflected XSS
->`"><img src=x onerror=alert(1)>` → another XSS attempt

How to Use

```bash
python3 scanner.py

url i tried:

http://localhost/dvwa/vulnerabilities/sqli/

Output
The result will shown:
scan_log.txt

known limitations:
	This is just a basic scanner. It won’t detect stored XSS or blind SQLi.
It’s mainly for educational purposes and beginner bug bounty practice.

currently it needs improvements.it doesnt support stored xxs and some other things.
it only goes through the form tag and inputbtag.most of the modern apps doesnt
 explictly include form or input tags.

it will be improved when i get deeper into the hacking automation stuff

About me:
	I’m Siddik, currently learning ethical hacking and cybersecurity. 
I built this as part of my 2-month study plan to strengthen my offensive 
security fundamentals.
