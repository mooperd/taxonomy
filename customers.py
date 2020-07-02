class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
    
    def print_details(self):
        print("{} lives in {} and their phone number is {}".format(self.name, self.address,self.phone_number))
    
    def return_dict(self):
        return_dict = {
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number
        }
        return return_dict


class Product:
    def __init__(self, name, weight, description, price):
        self.name = name
        self.weight = weight
        self.description = description
        self.price = price



customer_name = "Bobby Brown"
customers_address = "Wigan"
phone_number = "+4417440955744"

customer = Customer(customer_name, customers_address, phone_number)

print(customer.return_dict())

print(customer.print_details())