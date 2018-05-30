# shopping_cart.py
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)

#Checkpoint 1 - User Inputs

product_ids = []
total = 0

while True:
    try:
        product_id = input("Hey please input a product ID or 'DONE' if there are no more items:  ")
        if int(product_id) in range(0,len(products) + 1):
            product_ids.append(int(product_id))
        else:
            print("ERROR: Please check the Product ID and try again.")
            continue
    except:
        if product_id == "DONE":
            break


print("----------------------------")
print("H-MART")
print("----------------------------")
print("Visit us at www.h-mart.com")
print("Questions? Call us at 999.888.7654")
print("Checkout Time: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("----------------------------")
print("Items purchased:  ")

for x in product_ids:
    print ("+", products[x-1]['name'], '(${0:.2f})'.format(products[x-1]['price']))
    total += products[x-1]['price']


print("----------------------------")
print("Subtotal:  " + '${0:.2f}'.format(total))
print("Plus NYC Sales Tax (8.875%):  " + '${0:.2f}'.format(total*.08875))
print("Total:  " + '${0:.2f}'.format(total*1.08875))
print("----------------------------")
print("Thank you for your business. Please come again!")
#print("Visit us at www.h-mart.com")
#print("Questions? Call us at 999.888.7654")
print("----------------------------")
#print("Checkout Time: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("----------------------------")
#product_ids = [3, 12, 10, 3, 5, 11]

#def matching_product(product_identifier):
#    products_list = [product for product in products if product["id"] == product_identifier]
#    return products_list[0]
#raw_total = 0
#for pid in product_ids:
#    product = matching_product(int(pid))
#    #raw_total = raw_total + product["price"]
#    raw_total += product["price"]
#    print(str(product["id"]) + " " + product["name"] + ":" + " " + "$" + str(product["price"]))
#
#print("------------")
#print(raw_total)
#print("------------")
