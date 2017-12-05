from __future__ import print_function

import os
import sys
import json
import apiai

CLIENT_ACCESS_TOKEN = 'c7329636abe648c9ad117c83c0f3bb1f'


class ShoppingBot:
    itemsInfo = {}
    shoppingCart = None

    def __init__(self, data_file):
        self.shoppingCart = None
        print 'Start initializing shopping bot...'
        with open(data_file,'r') as f:
            for line in f.readline():
                s = line.split(',')
                itemsInfo[s[0]] = float(s[1])
        print 'Finished initializing shopping bot'

    def displayGreeting(self):
        print('Hi! Welcome to our grocery store! You can always type Help to get more information about our system!')

    def displayHelp(self):
        print('Buy something -- Say "add something to my cart"')

        print('Remove something -- Say "remove something"')

        print('List items in your shopping cart -- Type list-items')

        print('Check out -- Type checkout')

        print('Type exit to stop shopping')

    def displayItemsInCart(self):
        print(self.shoppingCart.toString)

    def displayBye(self):
        print('Thanks for shopping with us!')
        print('Bye')

    def askForQuantity(self, item):
        print('How many ' + item.unit + " do you want?")

    def run(self):
        self.displayGreeting()
        self.displayHelp()

        while True:
            print(u"> ", end=u"")

            userInput = raw_input()

            # normal flow
            if userInput.lower() == 'exit':
                self.displayBye()
                break
            elif userInput.lower() == 'list-items':
                self.displayItemsInCart()
            elif userInput.lower() == 'checkout':
                self.displayItemsInCart()
                self.displayBye()
            else:
                # send to aiapi
                ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

                request = ai.text_request()

                request.lang = 'en'  # optional, default value equal 'en'

                request.session_id = "1"

                request.query = userInput

                response = json.loads(request.getresponse().read())

                result = response['result']

                number = result['parameters']['number']

                print(response)

                items = result['parameters']['Item']

                if len(items) == 0:
                    print('Sorry, I don\'t understand.')
                    self.displayHelp()
                    pass

                if len(number) < len(items):
                    for itemName in items:
                        item = self.itemsInfo[itemName]
                        self.askForQuantity(item)

            print("echo " + userInput)


def main():
    shoppingBot = ShoppingBot("items.txt")

    shoppingBot.run()


if __name__ == '__main__':
    main()
