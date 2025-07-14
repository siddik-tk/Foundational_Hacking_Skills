from fpdf import FPDF
from datetime import datetime


logs = [
    {"url": "http://target.com/login", "payload": "' OR 1=1 --", "result": "Vulnerable"},
    {"url": "http://target.com/search", "payload": "<script>alert(1)</script>", "result": "Not Vulnerable"},
]


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Web Vulnerability Scan Report", ln=True, align='C')
pdf.ln(10)


timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Scan Time: {timestamp}", ln=True)
pdf.ln(5)


pdf.set_font("Arial", 'B', 12)
pdf.cell(80, 10, txt="URL", border=1)
pdf.cell(60, 10, txt="Payload", border=1)
pdf.cell(40, 10, txt="Result", border=1)
pdf.ln()


pdf.set_font("Arial", size=12)
for entry in logs:
    pdf.cell(80, 10, txt=entry["url"], border=1)
    pdf.cell(60, 10, txt=entry["payload"], border=1)
    pdf.cell(40, 10, txt=entry["result"], border=1)
    pdf.ln()

pdf.output(f"scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
