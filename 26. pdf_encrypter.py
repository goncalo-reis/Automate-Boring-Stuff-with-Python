import os, PyPDF2
from send2trash import send2trash

for root, folders, files in os.walk('D:\\Ambiente de Trabalho\\pdfs'):
    for file in files:
        if file.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfFileReader(os.path.join(root, file))
            for i in range(pdf_reader.numPages):
                page = pdf_reader.getPage(i)
                pdf_writer = PyPDF2.PdfFileWriter()
                pdf_writer.addPage(page)
            pdf_writer.encrypt('joel')
            file = f"{file.split('.pdf')[0]}_encrypted.pdf"
            with open(os.path.join(root, file), 'wb') as pdf:
                pdf_writer.write(pdf)
                print(f'{file} done.')

for root, folders, files in os.walk('D:\\Ambiente de Trabalho\\pdfs'):
    for file in files:
        if file.endswith('_encrypted.pdf'):
            try:
                pdf_reader = PyPDF2.PdfFileReader(os.path.join(root, file))
                pdf_reader.getPage(0)
                print(f'{file} not encrypted')
            except:
                print(f'{file} well encrypted')

for root, folders, files in os.walk('D:\\Ambiente de Trabalho\\pdfs'):
    for file in files:
        if file.endswith('_encrypted.pdf') == False:
            if file.endswith('.pdf'):
                send2trash(os.path.join(root, file))
                print(f'{file} sent to trash.')

print('Finished')

                    
