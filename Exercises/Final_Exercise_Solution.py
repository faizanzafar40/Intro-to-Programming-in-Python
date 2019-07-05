import sys
import os
import linecache
import datetime
import re


class Address:

    def __init__(self, street, house_number, postal_code, city):
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city

    def __str__(self):
        return self.street + " " + str(self.house_number) + \
            ", " + str(self.postal_code) + " " + self.city


class Credentials:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        ret = "Username: " + self.username + \
            " Password: " + "*" * len(self.password)

        return ret


class Customer:

    def __init__(self, name, age, street, house_number, postal_code, city,
                 username, password, cart=[]):
        self.name = name
        self.age = age
        self.cart = cart

        self.address = Address(street, house_number, postal_code, city)
        self.credentials = Credentials(username, password)

    def print_customer_information(self):

        print("Name: ", self.name)
        print("Age: ", str(self.age))
        print(self.address)
        print(self.credentials)

    def add_to_cart(self, cart):

        self.cart.append(cart)

    def show_cart(self):

        return self.cart

    def remove_from_cart(self, cart):

        self.cart.remove(cart)

    def place_order(self):

        print("Order placed successfully!")
        print("Your cart is now empty!")
        print("\n")

    
    def empty_cart(self):

        self.cart.clear()


class PrimeCustomer(Customer): #inheritance syntax

    def __init__(self, name, age, street, house_number, postal_code, city, username, password, expires_at):

        super().__init__(name, age, street, house_number, postal_code, city, username, password)
        self.expires_at = expires_at
        
        # we have to call constructor of super class in sub class when using inheritance

    def print_customer_information(self):

        super().print_customer_information()
        print("Membership expires at ", str(self.expires_at))


class NormalCustomer(Customer):

    def __init__(self, name, age, street, house_number, postal_code, city, username, password, is_hungry):
        super().__init__(name, age, street, house_number, postal_code, city, username, password)
        self.is_hungry = is_hungry

    def print_customer_information(self):

        super().print_customer_information()
        print("Hungry: ", "Yes" if self.is_hungry else "No") #pythonic way

def main_menu():

        i=1
        
        while(i!=0):
            
            print("<<<WELCOME TO AMAZON>>>")
            print("<<<MAIN MENU>>>\n")
            print("1. Register \n")
            print("2. Login \n")
            print("0. Exit \n")

            user_input_1 = int(input("Select your option from menu above: "))

            if(user_input_1==1):

                f_name = str(input("Enter first name: \n"))
                l_name = str(input("Enter last name: \n"))
                age = int(input("Enter age in years: \n"))
                s_add = str(input("Enter shipping address: \n"))
                typeofaccount = str(input("Enter type of account -> NORMAL or PRIME: \n"))
                
                email = str(input("Enter email ID: \n"))
                x = re.search("@", email)
                
                if (x):
                    u_name = str(input("Enter username: \n"))
                    p_word = str(input("Enter password: \n"))
                else:
                    print("You entered an invalid email \n")
                    print("User creation failed \n")
                
                try:
                    os.mkdir(u_name)
                except OSError:
                    print ("\nCreation of the user %s failed \n" % u_name)
                else:
                    print ("\nSuccessfully created the user %s \n" % u_name)

                path = u_name
                os.chdir(path)

                file1 = None
                
                try:
                    with open('secret.txt', 'w+') as file1:
                        file1.write(p_word)
                
                except FileNotFoundError as fnf:
                    print("File doesn't exist yet!")
                    pass
                finally:
                    if(file1 != None):
                        file1.close()

                file2 = None
                
                try:
                    with open('profile.txt', 'w+') as file2:
                        file2.write("first name: "+f_name+"\n")
                        file2.write("last name: "+l_name+"\n")
                        file2.write("age: "+str(age)+"\n")
                        file2.write("shipping address: "+s_add+"\n")
                        file2.write("Type of account: "+typeofaccount+"\n")
                        file2.write("Email: "+email+"\n")
                        file2.write(u_name)
                
                except FileNotFoundError as fnf:
                    print("User doesn't exist")
                except Exception as e:
                    pass
                finally:
                    if(file2 != None):
                        file2.close()

                os.chdir('..')

                file3 = None
                
                try:
                    with open('topdeals.txt', 'w+') as file3:
                        file3.write("1. Iphone"+"\n")
                        file3.write("2. SmartWatch"+"\n")
                        file3.write("3. Macbook"+"\n")
                        file3.write("4. Ipad"+"\n")

                except FileNotFoundError as fnf:
                    print("No top deals today :(")
                except Exception as e:
                    pass
                finally:
                    if(file3 != None):
                        file3.close()

                print("1. Register \n")
                print("2. Login \n")
                print("0. Exit \n")
                
                continue

            elif(user_input_1==2):
                
                input_username = str(input("Enter username: "))
                input_password = str(input("Enter password: "))

                path = input_username
                os.chdir(input_username)


                line_number = 7
                with open('profile.txt', 'r+') as filehandle:
                    current_line = 1
                    for line in filehandle:
                        if current_line == line_number:
                            file_username = line
                            break
                        current_line += 1

                with open('secret.txt', 'r+') as filehandle1:
                    file_password = filehandle1.read()

                login_count = 0
                
                if(input_username==file_username and input_password==file_password):
                    print("Login of user", input_username, "Successful!\n")
                    break
                
                elif(input_username==file_username and input_password!=file_password and login_count<3):
                    print("Password incorrect :(")
                    login_count = login_count + 1
                    continue
                
                elif(input_username!=file_username and input_password==file_password and login_count < 3):
                    print("Username incorrect :(")
                    login_count = login_count + 1
                    continue
                
                else:
                    print("Sorry your 3 login tries are over")
                    continue

            elif(user_input_1==0):

                print("See you next time!")
                quit()
        
        i=i+1


if __name__ == "__main__":
    
    d = datetime.datetime(2020, 10, 5, 18, 00)
    
    c1 = Customer("Anna Hermanns", 27, "Hafenallee", 50, 12345, "Mothers paradise", "anna_hermanns", "********")
    
    c2 = PrimeCustomer("Walter Herrlich", 58, "Turmstraße", 93, 23456, "Boring land", "w.herrlich1961", "********", expires_at=d)

    c3 = NormalCustomer("Unkwown identity", 33, "streetabc", 121, 34567, "NoMoneyLand", "catchmeifyoucan9000", "********", is_hungry=True)

    main_menu()

    os.chdir('..')

    def shopping_menu():

        j=1
 
        while(j!=0):
            
            print("<<<SHOPPING MENU>>> \n")
            print("1. Add to Cart \n")
            print("2. Show Top Deals \n")
            print("3. Display Cart \n")
            print("4. Logout \n" )
            print("0. Exit \n")

            user_input_2 = int(input("Select your option from menu above: "))

            if(user_input_2==1):

                enter_product = str(input("Enter the name of product you want to add to cart: "))
                c1.add_to_cart(enter_product)
                print("\n", enter_product, "added to cart successfully! \n")
                continue
            
            elif(user_input_2==2):

                with open('topdeals.txt', 'r+') as filehandle3:
                    top_deals = filehandle3.read()
                    print(top_deals)
                continue
            
            elif(user_input_2==3):

                print("Items in your shopping cart: ")
                print(c1.show_cart())
                print("\n")
                break

            elif(user_input_2==4):

                print("User has logged out successfully!\n")
                print("You are now back to: ")    
                main_menu()
            
            elif(user_input_2==0):

                print("See you next time!")
                quit()

        j=j+1

    
    shopping_menu()

    def display_cart_menu():
        
        k=1

        while(k!=0):
            
            print("<<<DISPLAY CART MENU>>> \n")
            print("1. Remove from Cart: \n")
            print("2. Checkout: \n")
            print("3. Go back to SHOPPING MENU: \n")
            print("0. Exit: \n") 

            user_input_3 = int(input("Select your option from menu above: "))

            if(user_input_3==1):

                remove_product = str(input("What would you like to remove from cart? "))
                c1.remove_from_cart(remove_product)
                print("\n", remove_product, "removed from cart successfully! \n")
                
                print("Updated shopping cart items:")
                print(c1.show_cart())
                print("\n")       
                continue

            elif(user_input_3==2):

                c1.place_order()
                c1.empty_cart()
                continue

            elif(user_input_3==3):

                print("You are now back to: ")    
                shopping_menu()
            
            elif(user_input_3==0):

                print("See you next time!")
                quit()

        k=k+1

    display_cart_menu()


                

