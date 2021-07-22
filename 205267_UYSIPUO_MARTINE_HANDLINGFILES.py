products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code, property):
    return products[code][property]

def main():
    with open("receipt.txt","w") as receipt:
        receipt.write('''
==
CODE\t\t\t\t\t\t\tNAME\t\t\t\t\t\t\tQUANTITY\t\t\t\t\tSUBTOTAL''')
        orders = {}
        total = 0
        while True:
            data = input(f"Please input the product code and quantity:")
            if data == "/":
                break
            else:
                product_code, quantity = data.split(",")
                add = orders.copy()
                add.update({product_code : [get_property(product_code, "name"), float(quantity), get_property(product_code, "price")*float(quantity)]})
                if len(set(add.keys())) == len(set(orders.keys())):
                    quantity = orders[product_code][1] + float(quantity)
                    orders[product_code][1] = quantity
                    orders[product_code][2] = get_property(product_code, "price")*float(quantity)
                    continue
                else:
                    orders.update({product_code : [get_property(product_code, "name"), float(quantity), get_property(product_code, "price")*float(quantity)]})
                    continue
        for i in orders:
            total += orders[i][2]

        for i in orders:
            receipt.write(f'''
{i}\t\t\t\t\t{orders[i][0]}\t\t\t\t\t{orders[i][1]}\t\t\t\t\t{orders[i][2]}''')

        receipt.write(f'''
Total:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{total}
==
        ''')
main()
