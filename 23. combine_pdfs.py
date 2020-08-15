import os, PyPDF2

pdf_writer = PyPDF2.PdfFileWriter()

x = 0
for file in os.listdir('D:\\Ambiente de Trabalho\\PDFS'):
    with open(os.path.join('D:\\Ambiente de Trabalho\\PDFS', file), 'rb') as pdf:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        for page_num in range(0 + x, pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
            with open('resultou.pdf', 'wb') as pdf:
                pdf_writer.write(pdf)
                x = 1


        
