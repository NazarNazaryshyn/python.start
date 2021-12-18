class item:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return f'Item - {self.name}, price - {self.price}$, size - {self.size}'

item_1 = item('Ball','12.3', '30cm')
item_2 = item('Shirt','15.99','70cm')
item_3 = item('Coat','29.99','100cm')


class customer:
    def __init__(self, name, lastname, middlename, age, phone):
        self.name = name
        self.lastname = lastname
        self.middlename = middlename
        self.age = age
        self.phone = phone

    def __str__(self):
        return f'{self.lastname} {self.name} {self.middlename} {self.age} years old, mobile phone - {self.phone}'

customer_1 = customer('Vitaliy','Kuzmenko','Vitaliyovich','22','+380674525347')
customer_2 = customer('Denis','Korsun','Illich','25','+380654323654')
customer_3 = customer('Adnriy','Rudiy','Mukolayovich','34','+380983421696')


class order:
    def __init__(self, customer, order, price ):
        self.customer_name = customer
        self.order_name = order
        self.order_price = price
    def __str__(self):
        return f'{self.order_name} ordered by {self.customer_name}, total price - {self.order_price}$'

order_1 = order(f'{customer_1.name} {customer_1.lastname}', item_2.name, item_2.price)
order_2 = order(f'{customer_2.name} {customer_2.lastname}', item_1.name, item_1.price)
order_3 = order(f'{customer_3.name} {customer_3.lastname}', item_3.name, item_3.price)



print(order_1)
print(order_2)
print(order_3)

