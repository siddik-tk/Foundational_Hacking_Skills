import nmap
import requests

scanner = nmap.PortScanner()
print("nmap scanner....")
print("<----------------------------------->")
ip_addr = input("enter the ip address to scan: ").strip()
print("your target ip address is ",ip_addr)
type(ip_addr)
response = input("""enter the type of scan you wan to perform ------------>
1.syn scan
2.udp scan
3.comprehensive scan
4.version detection
""")
print(" you have entered :  ",response)

if int(response) == 1:
    print("performing syn scan...")
    print("version: ",scanner.nmap_version())
    print(scanner.scan(ip_addr,'1-65500','-v -sS'))
    if 'tcp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['tcp'].keys())
    else:
        print("no open tcp ports found!")

elif int(response) == 2:
    print("performing UDP scan...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sU'))
    if 'udp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['udp'].keys())
    else:
        print("no open udp ports found!")

elif int(response) == 3:
    print("performing UDP scan...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sU'))
    if 'tcp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['tcp'].keys())
    else:
        print("no open tcp ports found!")

elif int(response) == 4:
    print("performing service detection...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sV '))
    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                print(f"""port:   {port} 
service: {service['name']}
vendor:  {service['product']}
version: {service.get('version',[])}
""")

else:
    print("scan invalid!")

print(scanner.scaninfo())
print("ip status is ",scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())

vuln_check = input("do you want to check the vulnerability information from the scan(y/n):  ").lower().strip()
def vuln_checker(vendor, version):
    url = f"https://vulnerability.circl.lu/api/browse/{vendor}"

    try:
        responses = requests.get(url)

        if responses.ok:
            data = responses.json()
            print(data)
            print('-'*50)
            cve_list = data.get("data", [])
            if cve_list:
                for cve in cve_list:
                    print(f"cve_id: {cve['id']} \n cve_summary: {cve['summary']}")
            else:
                print("no data found")
        else:
            print("unable to connect api (404)")
    except Exception :
        print("some error occured while fetching data from api!")

if vuln_check == "y":
    vendor = input("choose and input a vendor found in the scan: ")
    version = input("enter the version for the vendor: ")
    vuln_checker(vendor,version)
else:
    print("thank you!")
    print("come back anytime...")

# noinspection PyBroadException


