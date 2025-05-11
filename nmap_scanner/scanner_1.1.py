from fpdf import FPDF
from time import sleep
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

vendor_list = []
res_1 = {}
scan_data = {}
vendata = []

if int(response) == 1:
    print("performing syn scan...")
    print("version: ",scanner.nmap_version())
    print(scanner.scan(ip_addr,'1-65500','-v -sS'))
    scan_data = scanner.scan(ip_addr, '1-65500', '-v -sS')
    if 'tcp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['tcp'].keys())
        res_1 = scanner[ip_addr]['tcp'].keys()
    else:
        print("no open tcp ports found!")

elif int(response) == 2:
    print("performing UDP scan...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sU'))
    scan_data = scanner.scan(ip_addr, '1-65500', '-v -sU')
    if 'udp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['udp'].keys())
        res_1 = scanner[ip_addr]['udp'].keys()
    else:
        print("no open udp ports found!")

elif int(response) == 3:
    print("performing comprehensive scan...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sS -sV -sC -A'))
    scan_data = scanner.scan(ip_addr, '1-65500', '-v -sS -sV -sC -A')
    if 'tcp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['tcp'].keys())
        res_1 = scanner[ip_addr]['tcp'].keys()
    else:
        print("no open tcp ports found!")

elif int(response) == 4:
    print("performing service detection...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sV '))
    scan_data = scanner.scan(ip_addr, '1-65500', '-v -sV ')
    res_1 = scanner[ip_addr].keys()
    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                vendor = service.get('product','')
                if vendor:
                    vendor_list.append(vendor)
                print(f"""port:   {port} 
service: {service['name']}
vendor:  {service['product']}
version: {service.get('version',[])}
""")
                vend_details = [service['name'],service['product'],service.get('version',[])]
                vendata.append(vend_details)



else:
    print("scan invalid!")

print(scanner.scaninfo())
print("ip status is ",scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())

def vuln_checker(vendor):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    keyword = vendor

    params = {
        'keywordSearch': keyword,
        'ResultsPerPage': 5
    }

    res = requests.get(url, params=params)
    if res.ok:
        result = res.json()
        print(result)
        for lst in result.get('vulnerabilities',[]):
            cve_info = lst.get('cve',[])
            cve_id = cve_info.get('id',[])
            cve_desc = cve_info.get('descriptions','')


            print(f"cve id : {cve_id}")
            if cve_desc:
                print(f"cve description : {cve_desc[0].get('value', 'No description available')}")
            else:
                print("No description available.")

        feed = int(input("give a feed back(out of 5 in numbers):"))
        if feed < 3:
            print("we will improve")
        else:
            print("thanks for your useful time!")
    else:
        print("unable to fetch data from API(404)")
if int(response) == 4:
    vuln_check = input("do you want to check the vulnerability information from the scan(y/n):  ").lower().strip()

    if vuln_check == 'y':
        for vndor in vendor_list:
            vuln_checker(vndor)

class headers(FPDF):
    def header(self):
        self.set_font('helvetica', "", 16)
        self.cell(0,10,"--TechHunter log--",ln=1,align='c')
        self.ln(20)

    def footer(self):
        self.set_y(-20)
        self.set_font('helvetica',"",16)
        self.cell(0,10,f'page {self.page_no()}',align='c')



pdf = headers('p','mm','letter')
pdf.add_page()
pdf.set_auto_page_break(auto=True,margin=25)
pdf.set_font('helvetica',"",16)
pdf.cell(0,10,"NMAP SCANNER",ln=1,border=0,align='C')
pdf.cell(0,10,"VULNERABILITY CHECKER",ln=1,border=0,align='C')

pdf.cell(0,10,"scan summary: ")
pdf.ln(20)
pdf.multi_cell(200,10,f"overall scan result: {scan_data}")
pdf.ln(30)
pdf.cell(200,10,f"result of {response}: {res_1}")
if int(response) == 4:
    for data in vendata:
        pdf.ln(20)
        pdf.cell(200,10,f"service: {data[0]}",ln=1)
        pdf.cell(200, 10, f"vendor: {data[1]}",ln=1)
        pdf.cell(200, 10, f"version: {data[2]}",ln=1)


pdf.set_font('helvetica','B',30)
pdf.cell(0,50,text=" scan successful! ",align='c')

#127.0.0.1


pdf.output('pdf_2.pdf')