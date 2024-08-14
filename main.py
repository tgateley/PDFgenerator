import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation='P', unit="mm", format="A4")

df = pd.read_csv("topics.csv", sep=",")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    pdf.line(10,20,200,20)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
pdf.output("output.pdf")
