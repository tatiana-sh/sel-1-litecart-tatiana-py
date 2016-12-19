def test_cart_should_update_counter_on_add_remove_product(app):
    app.main_page.open()
    for cart_item in range(1, 4):
        app.main_page.click_product_in_campaign_section()
        app.product_page.add_item_of_size_to_cart(cart_item)
        app.main_page.open()

    app.cart_page.verify_cart_product_counter("3")

    app.cart_page.checkout_to_cart()
    for cart_item in range(1, 4):
        app.cart_page.remove_from_cart()
    app.main_page.open()

    app.cart_page.verify_cart_product_counter("0")
