Reconnaissance Toolchain

This folder contains the complete reconnaissance workflow I used during my bug bounty and security learning phase. It includes subdomain discovery, fingerprinting, target validation, and more.



Tools Covered

| Tool         | Purpose                          |
|--------------|----------------------------------|
| `assetfinder`| Subdomain discovery (passive)    |
| `subfinder`  | Subdomain discovery (advanced)   |
| `httpx`      | Domain validation & fingerprinting|
| `aquatone`   | Screenshotting live targets      |
| `xsstrike`   | XSS fuzzing                      |
| `ffuf`       | Parameter/dir fuzzing            |
| `dirsearch`  | Directory brute-forcing          |
| `burpsuite`  | Proxy-based recon                |
| `eyewitness` | Multi-protocol screenshotting    |
| `crt.sh`     | Passive subdomain enum (cert logs)|
| `HaveIBeenPwned` | Breach checking              |
| `Wappalyzer` | Tech stack fingerprinting        |
| `nikto`      | Misconfig & default file checks  |
| `securityheaders.com` | Header check            |

---

🧰 Usage Flow

1. Subdomain Discovery

Assetfinder
assetfinder --subs-only example.com > a.txt

Subfinder
subfinder -d example.com -silent > s.txt

Merge and dedupe
cat a.txt s.txt | sort -u > final_subs.txt
