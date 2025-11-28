def format_product_info(product_id, name, quantity, price):
    """
    Returns product information in a well-formatted string.

    Parameters:
        product_id (str or int): Unique product identifier
        name (str): Product name
        quantity (int or float): Amount of product in stock
        price (float): Price of the product

    Returns:
        str: Formatted product information
    """
    return (
        f"Product Information:\n"
        f"---------------------\n"
        f"Product ID : {product_id}\n"
        f"Name       : {name}\n"
        f"Quantity   : {quantity}\n"
        f"Price      : ${price:.2f}"
    )


# Example usage
if __name__ == "__main__":
    result = format_product_info(101, "Wireless Mouse", 25, 19.99)
    print(result)
