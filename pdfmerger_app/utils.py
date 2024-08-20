from PyPDF2 import PdfMerger


def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    with open(output_file, "wb") as f:
        merger.write(f)

    merger.close()
