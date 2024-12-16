import os
import subprocess

def convert_to_pdf(source_folder, output_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".doc") or filepath.endswith(".docx"):
                output_filepath = os.path.join(output_folder, os.path.splitext(file)[0] + ".pdf")
                command = f"/Applications/OpenOffice.app/Contents/MacOS/soffice --headless --convert-to pdf --outdir {output_folder} {filepath}"
                subprocess.run(command, shell=True)
                print(f"Converted {file} to PDF")

# Configura tus propias rutas de carpeta aquí
source_folder = 'docIn'  # Carpeta que contiene los archivos de Word
output_folder = 'docOut'  # Carpeta donde guardar los archivos PDF

convert_to_pdf(source_folder, output_folder)
