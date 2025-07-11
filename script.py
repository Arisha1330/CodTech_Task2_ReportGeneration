import csv
from fpdf import FPDF

# ✅ Step 1: Create data.csv (this avoids the file not found error)
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Department", "Score"])
    writer.writerow(["Alice", "IT", "85"])
    writer.writerow(["Bob", "HR", "90"])
    writer.writerow(["Charlie", "Finance", "78"])
    writer.writerow(["David", "Marketing", "88"])
    writer.writerow(["Eve", "Operations", "92"])

# ✅ Step 2: Define PDF generation class
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(200, 10, "Intern Report Summary", ln=True, align="C")
        self.ln(10)

    def add_table(self, data):
        self.set_font("Arial", size=12)
        col_widths = [40, 60, 30]
        for row in data:
            for j, item in enumerate(row):
                self.cell(col_widths[j], 10, txt=item, border=1)
            self.ln()

# ✅ Step 3: Read data from CSV
data = []
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

# ✅ Step 4: Create and save PDF
pdf = PDFReport()
pdf.add_page()
pdf.add_table(data)
pdf.output("report.pdf")

print("✅ PDF report generated as 'report.pdf'")
