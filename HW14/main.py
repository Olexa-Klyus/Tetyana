import product
import order
import customer

if __name__ == "__main__":
    try:
        milk = product.Product("milk", 25)
        grapefruit = product.Product("grapefruit", 75.25)
        chocolate = product.Product("chocolate", 45)
        customer = customer.Customer("Andrii", "35", "380_66_451_5878", "Lviv")

        print(grapefruit)
        print(customer)

        order = order.Order(customer)

        order.add_product(milk, 1)
        order.add_product(grapefruit, 3)
        order.add_product(chocolate, 2)

        print(order)

    except Exception as error:
        print(error)
