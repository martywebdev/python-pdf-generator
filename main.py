from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format='A4')

# adding page
pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)

pdf.cell(w=0, h=12, txt="hello there!", align="L", ln=1, border=0) #ln is the linebreak, height is suggested same as size

pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="hi there!", align="L", ln=1, border=0)


pdf.output('output.pdf')