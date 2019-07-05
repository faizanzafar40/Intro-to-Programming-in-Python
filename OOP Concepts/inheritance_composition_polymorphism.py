import sys


class Address:
    """ Class to store address information. """

    def __init__(self, street, house_number, postal_code, city):
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city

    def __str__(self):
        return self.street + " " + str(self.house_number) + \
            ", " + str(self.postal_code) + " " + self.city


class Credentials:
    """ Class to store user credentials. """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        ret = "Username: " + self.username + \
            " Password: " + "*" * len(self.password)

        return ret


class Customer:
    """ Amazon Customer class. """

    def __init__(self, name, age, street, house_number, postal_code, city,
                 username, password):
        self.name = name
        self.age = age

        # --- Concept of Composition
        self.address = Address(street, house_number, postal_code, city)
        self.credentials = Credentials(username, password)

    # Implement method print_customer_information which prints
    #       the customer information to screen in a well-arranged
    #       manner.
    def print_customer_information(self):
        print("Name: ", self.name)
        print("Age: ", str(self.age))
        print(self.address)
        print(self.credentials)


# Implement class PrimeCustomer, which inherits from class Customer.
#       This class has an additional date attribute 'membership', which stores
#       the membership expiry date.
#
#       Add methods print_membership_status() and print_customer_information().
class PrimeCustomer(Customer): #inheritance syntax
    def __init__(self, name, age, street, house_number, postal_code, city, username, password, expires_at):
        super().__init__(name, age, street, house_number, postal_code, city, username, password)
        self.expires_at = expires_at
        
        # we have to call constructor of super class in sub class when using inheritance

    def print_customer_information(self):
        super().print_customer_information()
        print("Membership expires at ", str(self.expires_at))

# Implement class NormalCustomer, which inherits from class Customer.
#       This class has an additional boolean attribute 'needs_food', which
#       indicates whether the person needs a food service.
#
#       Add methods is_hungry() and print_customer_information()


class NormalCustomer(Customer):
    def __init__(self, name, age, street, house_number, postal_code, city, username, password, is_hungry):
        super().__init__(name, age, street, house_number, postal_code, city, username, password)
        self.is_hungry = is_hungry

    def print_customer_information(self):
        super().print_customer_information()
        print("Hungry: ", "Yes" if self.is_hungry else "No") #pythonic way


if __name__ == "__main__":
    import datetime

    # Create basic customer object
    c1 = Customer("Anna Hermanns", 27, "Hafenallee", 50, 12345,
                  "Mothers paradise", "anna_hermanns", "********")

    # Create prime customer object
    d = datetime.datetime(2020, 10, 5, 18, 00)
    c2 = PrimeCustomer("Walter Herrlich", 58, "Turmstraße", 93, 23456,
                       "Boring land", "w.herrlich1961", "********", expires_at=d)

    # Create Normal customer object
    c3 = NormalCustomer("Unkwown identity", 33, "streetabc", 121, 34567,
                      "NoMoneyLand", "catchmeifyoucan9000", "********", is_hungry=False)

    # Create a list with all customer objects.

    customers = [c1, c2, c3]

    # Iterate through the list with customer objects
    #       and call method print_customer_information().

    for i in customers:
        i.print_customer_information()
