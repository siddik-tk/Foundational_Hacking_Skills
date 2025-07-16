import os

keywords = ['urgent', 'verify', 'reset', 'login', 'account locked', 'security alert']

def analyze_email(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read().lower()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    found = [word for word in keywords if word in content]

    print(f"\nScanning: {file_path}")
    if found:
        print(f"[!] ALERT: Suspicious keywords found: {found}")
    else:
        print("[-] No phishing keywords detected.")

def scan_folder(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.txt') or filename.endswith('.eml'):
            path = os.path.join(folder, filename)
            analyze_email(path)

scan_folder("/home/siddiktk/PycharmProjects/PythonProject/HACKING_FOUNDATION/DAY 29")
