from datetime import date
import datetime
import time

admindict = {'user': 'admin', 'password': 'admin'}
userdict = {0: {'Full name': 'Abhishek Verma', 'Mobile': 9771121340, 'Email id': 'abhishek534verma@gmail.com', 'Address': 'Delhi', 'Password': '12345'},1: {'Full name': 'Anshu Anand', 'Mobile': 7363747436, 'Email id': 'pandeyanshu@gmail.com', 'Address': 'Delhi', 'Password': '12345'}}
itemdict = {1: {'Food name': 'Tandoori Chicken', 'Quantity': '4 pieces', 'Price': 240, 'Discount': 10, 'Stock': 5},
          2: {'Food name': 'Vegan Burger', 'Quantity': '1 Piece', 'Price': 320, 'Discount': 5, 'Stock': 7},
          3: {'Food name': 'Truffle Cake', 'Quantity': '500gm', 'Price': 900, 'Discount': 12, 'Stock': 10}}
orderdict = {0: {'User id': 0, 'Food name': 'Tandoori Chicken', 'Quantity': '4 pieces', 'Price': 216, 'Date': datetime.date(2021, 8, 13), 'Time': '03:25:50'},
           1: {'User id': 0, 'Food name': 'Truffle Cake', 'Quantity': '500gm', 'Price': 792, 'Date': datetime.date(2021, 8, 13), 'Time': '03:25:50'},
           2: {'User id': 1, 'Food name': 'Vegan Burger', 'Quantity': '1 Piece', 'Price': 304, 'Date': datetime.date(2021, 8, 13), 'Time': '03:28:51'},
           3: {'User id': 1, 'Food name': 'Vegan Burger', 'Quantity': '1 Piece', 'Price': 304, 'Date': datetime.date(2021, 8, 13), 'Time': '03:28:51'},
           4: {'User id': 0, 'Food name': 'Tandoori Chicken', 'Quantity': '4 pieces', 'Price': 216, 'Date': datetime.date(2021, 8, 13), 'Time': '03:29:41'}}


# Order history
def order_history(ui):
    print('\nYour order history:-')
    for i in range(len(orderdict)):
        if orderdict[i]['User id'] == ui:
            print('Food name:', orderdict[i]['Food name'], '\tQuantity:', orderdict[i]['Quantity'], '\tPrice:',
                  orderdict[i]['Price'],
                  '\tDate:', orderdict[i]['Date'], '\tTime:', orderdict[i]['Time'], )


# Place new order
def place_order(ui):
    for i in range(1, len(itemdict) + 1):
        if itemdict[i]['Stock'] > 0:
            print('Menu no:', i, '\tFood name:', itemdict[i]['Food name'], '\tQuantity:', itemdict[i]['Quantity'],
                  '\tPrice: Rs.', itemdict[i]['Price'], '\t\tDiscount:', itemdict[i]['Discount'], '%')

    order = input('Enter your order using menu no(eg. 1,2)::').split(',')
    print('\nYour order preview::')
    total = 0
    for i in order:
        temp = int(i)
        rate = (itemdict[temp]['Price'] * (100 - itemdict[temp]['Discount'])) // 100
        total += rate
        print('Food name:', itemdict[temp]['Food name'], '\tQuantity:', itemdict[temp]['Quantity'],
              '\tPrice after discount: Rs.', rate)
    print('Your order total is:: Rs.', total)
    res = input('Enter yes to confirm your order or no to cancel::')

    if res == 'yes':
        for i in order:
            temp = int(i)
            rate = (itemdict[temp]['Price'] * (100 - itemdict[temp]['Discount'])) // 100
            today = date.today()
            now = datetime.datetime.now().strftime("%H:%M:%S")
            orderdict[len(orderdict)] = {'User id': ui, 'Food name': itemdict[temp]['Food name'], 'Quantity':
                itemdict[temp]['Quantity'], 'Price': rate, 'Date': today, 'Time': now}
        print('Order placed successfully :)')
    elif res == 'no':
        print('Order cancelled!!!')
    else:
        print('Error!!! Please re-place your order')
        place_order(ui)
    user_panel(ui)


# Update user profile
def update_profile(ui):
    print('\nYour profile::')
    print('Name:', userdict[ui]['Full name'])
    print('Mobile:', userdict[ui]['Mobile'])
    print('Email id:', userdict[ui]['Email id'])
    print('Address:', userdict[ui]['Address'])
    time.sleep(2)
    print('\nWhat detail you want to update::')
    print('1. Name')
    print('2. Mobile')
    print('3. Email id')
    print('4. Address')
    print('5. Password')
    print('6. go back')
    print('7. exit')
    choice = int(input("Enter your choice(1-5)::"))

    if choice == 1:
        temp = input('Enter your name::')
        userdict[ui]['Full name'] = temp
        print('Name update successful :)')
    elif choice == 2:
        temp = int(input('Enter your mobile number::'))
        userdict[ui]['Mobile'] = temp
        print('Mobile number update successful :)')
    elif choice == 3:
        temp = input('Enter your email id::')
        userdict[ui]['Email id'] = temp
        print('Email id update successful :)')
    elif choice == 4:
        temp = input('Enter your address::')
        userdict[ui]['Address'] = temp
        print('Address update successful :)')
    elif choice == 5:
        temp = input('Enter new paasword::')
        userdict[ui]['Password'] = temp
        print('Password update successful :)')
    elif choice == 6:
        user_panel(ui)
    elif choice == 7:
        print("Now terminating the program...")
        time.sleep(2)
        quit()
    else:
        print("Invalid input!!!")
    time.sleep(2)
    update_profile(ui)


# User Panel
def user_panel(ui):
    print("\nChoose Your Option")
    print("1. Place a new order")
    print("2. Your order history")
    print("3. Update your profile")
    print("4. Go back")
    print("5. Exit")
    choice = int(input("Enter your choice(1-5)::"))

    if choice == 1:
        place_order(ui)
    elif choice == 2:
        order_history(ui)
    elif choice == 3:
        update_profile(ui)
    elif choice == 4:
        user()
    elif choice == 5:
        print("Now terminating the program...")
        time.sleep(2)
        quit()
    else:
        print("Invalid input!!!")
    time.sleep(2)
    user_panel(ui)


# Check Id aand password validity for User
def user_check():
    email = input("Enter your Email id::")
    pwd = input("Enter your password::")
    flag = -1
    for i in range(len(userdict)):
        if userdict[i]['Email id'] == email and userdict[i]['Password'] == pwd:
            flag = i
            break
    if flag == -1:
        print("Wrong credentials!!!")
    return flag


# User Registration
def user_registration():
    print('Enter details:-')
    fname = input("Full name::")
    phone = int(input("Phone number::"))
    email = input("Email id::")
    add = input("Address::")
    pwd = input("Password::")
    userdict[len(userdict)] = {'Full name': fname, 'Mobile': phone, 'Email id': email, 'Address': add, 'Password': pwd}
    print("Account created successfully :)")


# User
def user():
    res = input("You want to login or register or exit or go back::")
    if res == 'login':
        flag = user_check()
        if flag != -1:
            print("Login Successful...")
            user_panel(flag)
    elif res == 'register':
        user_registration()
    elif res == 'go back':
        main()
    elif res == 'exit':
        print("Now terminating the program...")
        time.sleep(2)
        quit()
    else:
        print("Invalid input!!!")
    time.sleep(2)
    user()


# Remove item
def remove_item():
    res = int(input("Enter menu no::"))
    x = itemdict.keys()
    if res in x:
        for i in range(res, len(itemdict)):
            itemdict[i] = itemdict[i + 1]
            print("Item removed successfully :)")

        print("Updating menu now...")
        time.sleep(2)
        del itemdict[len(itemdict)]
        print("Menu updated successfully")

    else:
        print('Menu no not found!!!')


# View item details
def view_item():
    for i in range(1, len(itemdict) + 1):
        print('Menu no:', i, '\tFood name:', itemdict[i]['Food name'], '\tQuantity:',
              itemdict[i]['Quantity'], '\tPrice: Rs.', itemdict[i]['Price'], '\t\tDiscount:', itemdict[i]['Discount'],
              '%\t\tStock:', itemdict[i]['Stock'], 'unit(s)')


# Edit item Details
def edit_item():
    temp = int(input("\nEnter menu no::"))
    x = itemdict.keys()
    if temp in x:
        print('Enter updated details:-')
        fname = input("Food name::")
        quantity = input("Quantity per order::")
        price = int(input("Price(in rupees)::"))
        discount = int(input("Discount percentage::"))
        stock = int(input("Amount in stock::"))
        itemdict[temp] = {'Food name': fname, 'Quantity': quantity, 'Price': price, 'Discount': discount,
                          'Stock': stock}
        print("Book details updated successfully :)")
    else:
        print('Food Id not found!!!')
    time.sleep(2)


# Add item Details
def add_item():
    print('\nEnter item details:-')
    fname = input("Food name::")
    quantity = input("Quantity per order::")
    price = int(input("Price(in rupees)::"))
    discount = int(input("Discount percentage::"))
    stock = int(input("Amount in stock::"))

    itemdict[len(itemdict) + 1] = {'Food name': fname, 'Quantity': quantity, 'Price': price,
                                   'Discount': discount, 'Stock': stock}

    print("New item added to menu successfully :)")
    time.sleep(2)


# Admin Panel
def admin_panel():
    print("\nChoose Your Option")
    print("1. Add new item")
    print("2. Edit item")
    print("3. View all items")
    print("4. Remove item")
    print("5. Go back")
    print("6. Exit")
    choice = int(input("Enter your choice(1-6)::"))

    if choice == 1:
        add_item()
    elif choice == 2:
        edit_item()
    elif choice == 3:
        view_item()
    elif choice == 4:
        remove_item()
    elif choice == 5:
        main()
    elif choice == 6:
        print("Now terminating the program...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input!!!")
    time.sleep(2)
    admin_panel()


# Check Id aand password validity for Admin
def admin_check():
    uname = input("Enter your username::")
    pwd = input("Enter your password::")
    flag = -1

    if admindict['user'] == uname and admindict['password'] == pwd:
        flag = 1

    if flag == -1:
        print("Wrong credentials!!!")
        admin_check()
    return flag


# Main function
def main():
    usertype = input("Who are you(admin or user) or exit::")

    # Admin type
    if usertype == 'admin':
        flag = int(admin_check())
        if flag == 1:
            print("Login Successful...")
            admin_panel()

    elif usertype == 'user':
        user()

    elif usertype == 'exit':
        print("Now terminating the program...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input!!!\nPlease try again...")
    time.sleep(2)
    main()


# Start of Food Ordering App
print("*****WECLOME TO FOOD ORDERING APP*****")
main()