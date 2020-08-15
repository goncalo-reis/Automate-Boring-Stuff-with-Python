import PyPDF2

words = []
words_lower = []
with open('D:\\Ambiente de Trabalho\\dictionary.txt', 'r') as file:
    words_upper = file.read().split('\n')
    for word in words_upper:
        words.append(word)
        words_lower.append(word.lower())
    for word in words_lower:
        words.append(word)
x = 0
y = 500
for word in words:
    pdf_reader = PyPDF2.PdfFileReader('D:\\Ambiente de Trabalho\\pdfs\\meetingminutes_encrypted.pdf')
    decryption = pdf_reader.decrypt(word)
    x += 1
    if x == y:
        print(f'{str(y)} words')
        y += 500
    if decryption == 1:
        print(f'Done. Password was {word}')
        break
