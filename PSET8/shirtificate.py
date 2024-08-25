from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")

    def add_image(self, text):
        self.image("shirtificate.png", x=10, y=50, w=190)
        self.set_font("Arial", "B", 24)
        self.set_y(140)
        self.cell(0, 10, f"{text} took CS50", ln=True, align="C")


pdf = PDF()

# Add a page
pdf.add_page()


# User-input text
user_text = input("Enter the text you want on the shirt: ")

# Add the shirt and text to the PDF
pdf.add_image(user_text)

# Save the PDF
pdf.output("shirtificate.pdf")
