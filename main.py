import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation='P', unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv", sep=",")

for index, row in df.iterrows():
    pdf.add_page()

    # Sets the Header
    pdf.set_font(family="Times", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    pdf.line(10,20,200,20)

    for y in range(20, 280, 10):
        pdf.line(10, y, 200, y)
# Sets the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for y in range(20, 280, 10):
            pdf.line(10, y, 200, y)
    # Sets the Footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
pdf.output("output.pdf")
