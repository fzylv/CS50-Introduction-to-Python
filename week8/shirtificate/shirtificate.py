from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", style="B", size=30)
        self._pdf.cell(0, 50, 'CS50 Shirtificate.', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", x=10, y=100, w=190)
        self._pdf.set_font("helvetica", size=30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=70, y=165, txt=f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
