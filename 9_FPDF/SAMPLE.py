import nmap
import requests
from fpdf import FPDF
from time import sleep



class headers(FPDF):
    def header(self):
        self.image('kali_logo.png',10,10,20)
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
pdf.cell(100,10,"hacking...",ln=1,border=1,align='C')
pdf.cell(100,10,"completing...",ln=1,border=1,align='C')

for i in range(0,101,4):
    pdf.cell(0,10,f"exploiting...{i}%",ln=True)
    print(f"exploiting...{i}%")
    sleep(0.2)
pdf.set_font('helvetica','B',60)
pdf.cell(0,50,text=" system hacked! ",align='c')

pdf.output('pdf_1.pdf')