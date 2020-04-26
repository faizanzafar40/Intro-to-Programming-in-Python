'''
Write a Amazon Customer class which can do basic customer operations


when using with statement - no need to close the file
put file.close() in finally block else it wil stay in memory
readlines() returns a list of lines
.append() makes a nested list
.extend() enlarges the original list
.append() and extend() return type None i.e. modify the original list

'''



class Customer():
    def __init__(self, name, email="na", age="na", address="na",cart=[]):
        self.name = name
        self.email = email
        self.age = age
        self.address = address
        self.cart = cart
    
    def add_to_cart(self, cart):
        self.cart.append(cart)
        print (cart, "added for", self.name)
    
    def show_cart(self):
        return self.cart
    
    def remove_from_cart(self, cart):
        self.cart.remove(cart)
        print (cart, "removed for", self.name)
    
    def place_order(self):
        print("Order placed successfully!")



cust = Customer("faizan")

cust.add_to_cart("Pixel Xl 3")

cust.add_to_cart("IPhone")

cust.add_to_cart("Macbook")

print("Selected items", cust.show_cart())

cust.remove_from_cart("IPhone")

print("Selected items", cust.show_cart())

cust.place_order()