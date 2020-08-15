import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

county_data = {}

for row in range(2, sheet.max_row + 1):
    state = sheet[f'B{str(row)}'].value
    county = sheet[f'C{str(row)}'].value
    population = sheet[f'D{str(row)}'].value
    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts' : 0, 'population' : 0})
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['population'] += int(population)

file = open('census.py', 'w')
file.write(f'allData = {pprint.pformat(county_data)}')
file.close()
    
