import PyPDF2
import sys

pdf_file_list = sys.argv[1:]
watermark = 'wtr.pdf'
output = "watermarked.pdf"
for file in pdf_file_list:
    with open(file, 'rb') as fileinput:
        pdf_file = PyPDF2.PdfFileReader(fileinput)
        with open(watermark, 'rb') as filewatermark:
            watermark_pdf = PyPDF2.PdfFileReader(filewatermark)
            # print(pdf_file.getNumPages())
            for page in range(pdf_file.getNumPages()):
                #     print(page)
                current_page = pdf_file.getPage(0)
                first_page_watermark = watermark_pdf.getPage(0)
                current_page.mergePage(first_page_watermark)
                pdf_writer = PyPDF2.PdfFileWriter()
                pdf_writer.addPage(current_page)
                with open(output, 'wb')as file_output:
                    pdf_writer.write(file_output)
