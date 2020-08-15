import os, shutil, natsort

oldList = ['placeHolder']
newList = ['place_holder']

z = 1
while newList != oldList:
    oldList = []
    newList = []
    for file in os.listdir('teste'):
        oldList.append(file)
    oldList = natsort.natsorted(oldList)
    y = 0
    i = 1
    x = 0
    while oldList[-1] != 'spam' + str(i) + '.txt' or oldList == []:    
        oldName = 'teste\\spam' + str(i) + '.txt'
        if os.path.exists(oldName) == True:
            i += 1
        elif y == 0:
            try:
                source = 'teste\\spam' + str(i + z) + '.txt'
                destination = 'teste\\spam' + str(i) + '.txt'
                shutil.move(source, destination)
                i += 1
                z += 1
                y += 1
                break
            except FileNotFoundError:
                x += 1
                try:
                    source = 'teste\\spam' + str(i + z + x) + '.txt'
                    destination = 'teste\\spam' + str(i) + '.txt'
                    shutil.move(source, destination)
                    y += 1
                    i += 1
                    z += 1
                    break
                except FileNotFoundError:
                    print('retry')
                    continue    
    for file in os.listdir('teste'):
        newList.append(file)
    newList = natsort.natsorted(newList)
    print(oldList)
    print(newList)
    print()
