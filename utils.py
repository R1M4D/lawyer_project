def calculate_total_from_cart(cart):
    total_cart_price = 0
    total_cart_count = 0
    for cart_item in cart:
        total_cart_price += cart_item.get('price') * cart_item.get('count')
        total_cart_count += cart_item.get('count')

    return {
        "price": total_cart_price,
        "count": total_cart_count
    }