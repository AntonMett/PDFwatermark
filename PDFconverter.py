import PyPDF2
import sys
from os import remove

pdf_file_list = sys.argv[1:]
watermark = 'wtr.pdf'
merger = PyPDF2.PdfFileMerger()
writer = PyPDF2.PdfFileWriter()


for file in pdf_file_list:
    merger.append(file)

merger.write('super.pdf')


with open('super.pdf', 'rb') as fileinput:
    pdf_file = PyPDF2.PdfFileReader(fileinput)

    with open(watermark, 'rb') as filewatermark:
        watermark_pdf = PyPDF2.PdfFileReader(filewatermark)

        for page in range(pdf_file.getNumPages()):
            current_pdf_page = pdf_file.getPage(page)
            first_page_watermark = watermark_pdf.getPage(0)
            current_pdf_page.mergePage(first_page_watermark)
            writer.addPage(current_pdf_page)

            with open("watermarked.pdf", 'wb')as file_output:
                writer.write(file_output)
                remove('super.pdf')
