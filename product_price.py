from amazon_bot import AmazonBot

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class PriceUpdater(object):
    def __init__(self, spreadsheet_name):
        self.items_column = 1
        self.price_column = 2
        self.frequency_column = 3
        self.url_column = 4
        self.product_name_column = 5

        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name).sheet1

    def process_item_list(self):
        items = self.sheet.col_values(self.items_column)[1:]

        amazon_bot = AmazonBot(items)
        prices, urls, names = amazon_bot.search_items()

        print('Updating spreadsheet.')
        for i in range(len(prices)):
            self.sheet.update_cell(i+2, self.price_column, prices[i])
            self.sheet.update_cell(i+2, self.url_column, urls[i])
            self.sheet.update_cell(i+2, self.product_name_column, names[i])
