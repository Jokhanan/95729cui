class Cart():
    def __init__(self):
        self.items = {}

    '''
	add item to shopping cart 
	'''

    def addToCart(self, item):
        if item.itemName in self.items:
            new_quantity = item.getQuantity()
            old_quantity = self.items[item.itemName].getQuantity()
            self.items[item.itemName].setQuantity(new_quantity + old_quantity)
        else:
            name = item.itemName
            self.items[name] = item
        return
    '''
    
    '''
    def editCart(self,item,amount):
        if item.itemName not in self.items:
            print (item.itemName + " not in shopping cart! ")
            return False

        else:
            number = self.items[item.itemName].getQuantity()
            if number <= amount:
                self.items.pop(item.itemName)
            else:
                self.items[item.itemName].setQuantity(number - amount)

        return True

    '''
	remove item from shopping cart, item is a string 
	'''

    def removeItem(self, item):
        if item not in self.items:
            print item + " not in shopping cart"
            return False
        self.items.pop(item)
        return True

    '''
	Print every item + quantity in the shopping cart. 
	'''

    def toString(self):
        lst = []
        for (k, item) in self.items.iteritems():
            lst.append((k, item.getQuantity()))
        print (lst)
        return

    '''
	list everything in the shopping cart 
	'''

    def printCart(self):
        print 'name      quantity        price'
        for (k, item) in self.items.iteritems():
            name = k
            quantity = item.getQuantity()
            price = item.getPrice()
            totalP = float(quantity) * price
            print name + "          " + str(quantity) + "           " + str(totalP)
        return

    def getTotal(self):
        total = 0
        for (k, item) in self.items.iteritems():
            total += item.getQuantity() * item.getPrice()
        print '--------------------------------------'
        print 'total amount ' + str(total)
        self.items.clear()
        return
