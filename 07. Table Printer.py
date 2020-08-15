tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

rowNum = len(tableData)
colNum = len(tableData[0])
maxLengthItem = 0
maxLengthList = []

for list in tableData:
    for item in list:
        if len(item) > maxLengthItem:
            maxLengthItem = len(item)
    maxLengthList.append(maxLengthItem)

for row in range(colNum):
    print()
    for column in range(rowNum):
        print(tableData[column][row].rjust(maxLengthList[column]), end=' ')
