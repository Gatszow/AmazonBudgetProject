import product_price
import email_alert

if __name__ == '__main__':
    price_updater = product_price.PriceUpdater('ProductPrice')
    price_updater.process_item_list()

    name_of_spreadsheet = 'ProductPrice'
    email = email_alert.EmailAlert('Google Sheets Updated',
                                   'Spreadsheet {} has been updated'.format(name_of_spreadsheet))

    email.send_email()
