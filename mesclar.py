import PyPDF2
import os

merger = PyPDF2.PdfFileMerger(strict=False)

lista_arquivo = os.listdir("arquivos")
for arquivo in lista_arquivo:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")
merger.write("Pdf_final.pdf")