import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merge.pdf')


pdf_combine(inputs)
watermark = 'wtr.pdf'


def watermark_page():
    with open(watermark, 'rb') as filegale
