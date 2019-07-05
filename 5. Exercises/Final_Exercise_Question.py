"""Amazon App

Write a program that mimics Amazon, with following features:


- Top Menu =>
    1. Register
    2. Login
    0. Exit

- 1. Register
    - Input firstname, lastname, age, shipping address, email, password, type of account(prime or normal),
    - (Optional) Validate above mentioned inputs, (Hint: checkout python builtin 're' package for regular expressions)
    - Create a separate directory for that user (secret.txt for storing hash password, profile.txt for rest of the user info)
    e.g directory structure should loook like:
        george =>
                secret.txt
                profile.txt

        thomas =>
                secret.txt
                profile.txt
        topdeals.txt    <--- should contain top deals

- 2. Login
    - Check user credentials (i.e username and password) in that particular user directory  (secret.txt for password)
    - only three login attempts should be allowed
    - after successful login show Second Menu

- Second Menu =>
    1. Add to Cart
    2. Show Top Deals
    3. Display Cart
    4. Logout   <--- note it goes back to login menu
    0. Exit

- 1. Add to Cart
    Enter the product you want to add:

- 2. Show Top Deals
    1. Iphone
    2. SmartWatch
    3. Macbook
    4. Ipad
    0. <Back>    <--- it goes back to second menu



- 3. Display Cart =>
    [iPhone, Macbook]
    1. Remove from Cart <--- asks which product to remove
    2. Checkout <--- display your order was successful and clear the cart
    0. <Back>    <--- it goes back to second menu


Hints:
    - Use separate classes
    - there is no one fix solution, use your imagination
    - some possible classes are: Customer, Order, ShoppingCart etc.
    - Use python builtin module "os" to create directory (e.g os.mkdir('directory name'))




"""