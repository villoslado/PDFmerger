from PyPDF2 import PdfMerger


def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()


pdf_files = ["file1.pdf", "file2.pdf"]
merge_pdfs(pdf_files, "merged.pdf")
