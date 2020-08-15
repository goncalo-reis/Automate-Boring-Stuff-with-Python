inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        total += value
    print('Total number of items: ' + str(total))
    print()
  
def addToInventory(inventory, list):
    print('Inventory updated:')
    for loot in list:
        if loot in inventory:
            inventory[loot] += 1
        else:
            inventory[loot] = 1
    newTotal = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        newTotal += value
    print('Total number of items: ' + str(newTotal))
    print()

displayInventory(inventory)
addToInventory(inventory, dragonLoot)




