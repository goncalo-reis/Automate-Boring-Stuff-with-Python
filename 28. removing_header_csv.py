import csv, os

root = 'D:\\Ambiente de Trabalho\\csvs'
os.makedirs('D:\\Ambiente de Trabalho\\novos')
new_root = 'D:\\Ambiente de Trabalho\\novos'
for file in os.listdir(root):
    with open(os.path.join(root, file)) as csv_file:
        rows = []
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if csv_reader.line_num == 1:
                continue
            print(row)
            rows.append(row)
        with open(os.path.join(new_root, file), 'w', newline='') as new_csv:
            csv_writer = csv.writer(new_csv)
            for row in rows:
                csv_writer.writerow(row)
