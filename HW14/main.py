import product_App
import order_App
import customer_App

if __name__ == "__main__":
    try:
        milk = product_App.Product("milk", 25)
        grapefruit = product_App.Product("grapefruit", 75.25)
        chocolate = product_App.Product("chocolate", 45)
        customer = customer_App.Customer("Andrii", "35", "380_66_451_5878", "Lviv")

        print(grapefruit)
        print(customer)
        print('----------------------------')

        order = order_App.Order(customer)

        order.add_product(milk, 1)
        order.add_product(grapefruit, 3)
        order.add_product(chocolate, 2)

        print(order)

    except Exception as error:
        print(error)
