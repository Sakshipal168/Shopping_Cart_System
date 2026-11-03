"""
PS 7 - Shopping Cart System
Console-based shopping cart: view products, add/remove items, and
generate a final bill with discount and GST.
"""

# Product catalogue (dictionary)
PRODUCTS = {"Pen": 10, "Notebook": 50, "Bag": 500}

GST_RATE = 0.18          # 18% GST  
DISCOUNT_RATE = 0.10     # 10% discount
DISCOUNT_LIMIT = 500     # discount applies if subtotal is more than this

# Cart: {product_name: quantity}
cart = {}


def format_number(value):
    """Show whole numbers without decimals (590 instead of 590.0)."""
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.2f}"


def find_product(name):
    """Return the catalogue name for the input (case-insensitive) or None."""
    name = name.strip().title()
    return name if name in PRODUCTS else None


def get_subtotal():
    return sum(PRODUCTS[item] * qty for item, qty in cart.items())


def view_products():
    print("\n--- Available Products ---")
    for name, price in PRODUCTS.items():
        print(f"{name:<10} Rs.{price}")


def cart_summary():
    """One-line cart description, e.g. 'Bag x2 = 1000'."""
    if not cart:
        return "empty"
    return ", ".join(
        f"{item} x{qty} = {format_number(PRODUCTS[item] * qty)}"
        for item, qty in cart.items()
    )


def add_to_cart(name, quantity):
    product = find_product(name)
    if product is None:
        print(f"Invalid product. Available: {', '.join(PRODUCTS)}")
        return
    if quantity < 1:
        print("Quantity must be at least 1.")
        return
    cart[product] = cart.get(product, 0) + quantity
    print(f"{product} x{quantity} added | Cart subtotal: {format_number(get_subtotal())}")


def remove_from_cart(name):
    product = find_product(name)
    if product is None:
        print(f"Invalid product. Available: {', '.join(PRODUCTS)}")
        return
    if product not in cart:
        print(f"{product} is not in the cart.")
        return
    del cart[product]
    print(f"{product} removed. Cart: {cart_summary()}")


def view_cart():
    print("\n--- Your Cart ---")
    if not cart:
        print("Cart is empty.")
        return
    for item, qty in cart.items():
        price = PRODUCTS[item]
        print(f"{item:<10} Rs.{price} x {qty} = Rs.{format_number(price * qty)}")
    print(f"Cart subtotal: Rs.{format_number(get_subtotal())}")


def calculate_bill():
    """Return (subtotal, discount, gst, grand_total)."""
    subtotal = get_subtotal()
    discount = subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_LIMIT else 0
    gst = (subtotal - discount) * GST_RATE
    grand_total = subtotal - discount + gst
    return subtotal, discount, gst, grand_total


def checkout():
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return
    subtotal, discount, gst, grand_total = calculate_bill()
    print("\n========== FINAL BILL ==========")
    for item, qty in cart.items():
        print(f"{item:<10} x{qty:<3} Rs.{format_number(PRODUCTS[item] * qty)}")
    print("--------------------------------")
    print(
        f"Subtotal: {format_number(subtotal)} | "
        f"Discount: {format_number(discount)} | "
        f"GST: {format_number(gst)}"
    )
    print(f"Grand Total: {format_number(grand_total)}")
    print("================================")
    cart.clear()


def read_quantity():
    """Read an integer quantity from the user; return None if not a number."""
    try:
        return int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be a whole number.")
        return None


def main():
    while True:
        print("\n===== SHOPPING CART MENU =====")
        print("1. View products")
        print("2. Add to cart")
        print("3. Remove from cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            view_products()
        elif choice == "2":
            name = input("Enter product name: ")
            quantity = read_quantity()
            if quantity is not None:
                add_to_cart(name, quantity)
        elif choice == "3":
            remove_from_cart(input("Enter product name to remove: "))
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
