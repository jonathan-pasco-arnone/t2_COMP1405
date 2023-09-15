""" Module file for sales analysis """

# Created by: Jonathan Pasco-Arnone
# Created on: September 2023

import linecache # allows me to easily get the contents of each line

def get_number_purchases(filename):
    """Retrieves the number of purchases (aka amount of customers)"""
    total_purchases = 0
    current_name_line = 1 # First name is on line 1 and not 0
    while linecache.getline(filename, current_name_line) != "":
        total_purchases += 1
        current_name_line += 6
    return total_purchases

def get_total_purchases(filename):
    """Retrieves the total cost of all purchases"""
    total_price = 0
    current_name_line = 6 # First total cost is on line 6
    while linecache.getline(filename, current_name_line) != "":
        total_price += int(linecache.getline(filename, current_name_line))
        current_name_line += 6
    return total_price

def get_average_purchases(filename):
    """Finds the average cost of the purchases"""
    if get_total_purchases(filename) == 0:
        return 0
    else:
        return get_total_purchases(filename) / get_number_purchases(filename)

def get_number_customer_purchases(filename, customer):
    """Finds the number of purchases made by a specific customer"""
    total_purchases_from_customer = 0
    current_name_line = 1 # First name is on line 1 and not 0
    while linecache.getline(filename, current_name_line) != "":
         # The \n is required because the linecach.getline function
         # automatically appends a \n to the end of the string that it reads
        if linecache.getline(filename, current_name_line) == (customer + "\n"):
            total_purchases_from_customer += 1
        current_name_line += 6
    return total_purchases_from_customer

def get_total_customer_purchases(filename, customer):
    """Gets the total number of items that have been purchased by a specific customer"""
    total_price_from_customer = 0
    current_name_line = 1 # First name is on line 1 and not 0
    while linecache.getline(filename, current_name_line) != "":
         # The \n is required because the linecach.getline function
         # automatically appends a \n to the end of the string that it reads
        if linecache.getline(filename, current_name_line) == (customer + "\n"):
            # If the name matches the inputed customer then it will add their
            # total cost (which is found 5 lines below their name)
            total_price_from_customer += int(linecache.getline("./sales-stats/"
                  + filename, current_name_line + 5))
        current_name_line += 6
    return total_price_from_customer

def get_average_customer_purchases(filename, customer):
    """Finds the average cost of all the purchases made by a specific customer"""
    if get_total_customer_purchases(filename, customer) == 0:
        return 0
    else:
        return (get_total_customer_purchases(filename, customer)
              / get_number_customer_purchases(filename, customer))

def get_most_popular_product(filename):
    """Finds which product has the most sales"""
    desktop_amount = 0
    laptop_amount = 0
    tablet_amount = 0
    toaster_amount = 0
    return_value = ""
    current_line = 2 # First product starts at line 2
    while linecache.getline(filename, current_line) != "":
        desktop_amount += int(linecache.getline(filename, current_line))
        current_line += 1 # Cycle to the next product
        laptop_amount += int(linecache.getline(filename, current_line))
        current_line += 1
        tablet_amount += int(linecache.getline(filename, current_line))
        current_line += 1
        toaster_amount += int(linecache.getline(filename, current_line))
        current_line += 3 # Cycle to the next customer
    if (desktop_amount >= laptop_amount and desktop_amount > tablet_amount
          and desktop_amount > toaster_amount):
        return_value = "Desktop"
    elif laptop_amount >= tablet_amount:
        if laptop_amount > toaster_amount:
            return_value = "Laptop"
    elif tablet_amount >= toaster_amount:
        return_value = "Tablet"
    else:
        return_value = "Toaster"
    return return_value
