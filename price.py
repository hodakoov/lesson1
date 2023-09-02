def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

r = format_price(56.24)
print(r)