import openpyxl, os
os.chdir('D:\\Ambiente de Trabalho')

workbook = openpyxl.load_workbook('produceSales.xlsx')
sheet = workbook['Sheet']

for row in range(2, sheet.max_row + 1):
    produce = sheet[f'A{row}'].value
    if produce == 'Celery':
        sheet[f'B{row}'] = 1.19
    if produce == 'Garlic':
        sheet[f'B{row}'] = 3.07
    if produce == 'Lemon':
        sheet[f'B{row}'] = 1.27
workbook.save('updatedProduceSales.xlsx')

