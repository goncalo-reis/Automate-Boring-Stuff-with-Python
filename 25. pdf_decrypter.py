import PyPDF2, os
from send2trash import send2trash

for root, folders, files in os.walk('D:\\Ambiente de Trabalho\\pdfs'):
    for file in files:
        if file.endswith('_encrypted.pdf'):
            pdf_reader = PyPDF2.PdfFileReader(os.path.join(root, file))
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_reader.decrypt('Joel')
            for i in range(pdf_reader.numPages):
                page = pdf_reader.getPage(i)
                pdf_writer.addPage(page)
            file = f"{file.split('_encrypted.pdf')[0]}.pdf"
            with open(os.path.join(root, file), 'wb') as pdf:
                pdf_writer.write(pdf)

for root, folders, files in os.walk('D:\\Ambiente de Trabalho\\pdfs'):
    for file in files:
        if file.endswith('_encrypted.pdf') == False:
            if file.endswith('pdf'):
                pdf_reader = PyPDF2.PdfFileReader(os.path.join(root, file))
                pdf_reader.getPage(0)
                print(f'{file} decrypted.')

for root, folders, files in os.walk('D:\\Ambiente de Trabalho\\pdfs'):
    for file in files:
        if file.endswith('_encrypted.pdf'):
            send2trash(os.path.join(root, file))

print('Finished.')

