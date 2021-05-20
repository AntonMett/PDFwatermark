import PyPDF2
import sys

pdf_file_list = sys.argv[1:]
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()
for file in pdf_file_list:
    pdf_file = PyPDF2.PdfFileReader(open(file, 'rb'))
    for page in range(pdf_file.getNumPages()):
        each_page = pdf_file.getPage(page)
        each_page.mergePage(watermark.getPage(0))
        output.addPage(each_page)
        watermarked_file = open('watermarked_file.pdf', 'rw')
        output.write(watermarked_file)
