
# convertir .doc a pdf:
# /Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf --outdir /Users/dani/Projectes/wordsTOpdf/pdf  /Users/dani/Projectes/wordsTOpdf/docIn/*.doc

from PyPDF2 import PdfMerger
import os
from datetime import datetime

# Carpeta amb els PDFs generats
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
pdf_folder = "/Users/dani/Projectes/wordsTOpdf/pdf"
output_pdf = f"/Users/dani/Projectes/wordsTOpdf/docOut/combined_{current_time}.pdf"

# Crear un objecte PdfMerger
merger = PdfMerger()

# Afegir cada PDF al fitxer combinat
for pdf_file in sorted(os.listdir(pdf_folder)):
    if pdf_file.endswith(".pdf"):
        merger.append(os.path.join(pdf_folder, pdf_file))

# Escriure el PDF combinat
merger.write(output_pdf)
merger.close()

print(f"El PDF combinat s'ha desat a: {output_pdf}")