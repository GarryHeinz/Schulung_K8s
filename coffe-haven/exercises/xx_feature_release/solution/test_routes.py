from app.routes import PRODUCTS, PROMO_CODES

HTTP_OK = 200


def test_index_page(client):
    """Test the index page loads and displays products correctly."""
    response = client.get("/")

    assert response.status_code == HTTP_OK
    assert b"Espresso Machine" in response.data
    assert b"Pour-Over Coffee Maker" in response.data


def test_cart_page_empty(client):
    """Test the cart page when it's empty."""
    response = client.get("/cart")

    assert response.status_code == HTTP_OK
    assert b"Your cart is empty" in response.data


def test_cart_page_with_items(client):
    """Test the cart page after items are added."""
    product = next(p for p in PRODUCTS if p["id"] == 1)
    client.get("/add/1")
    response = client.get("/cart")

    assert response.status_code == HTTP_OK
    assert b"Your Cart" in response.data
    assert product["name"].encode() in response.data


def test_add_to_cart(client):
    """Test adding an item to the cart."""
    product = next(p for p in PRODUCTS if p["id"] == 1)
    response = client.get("/add/1", follow_redirects=True)

    assert response.status_code == HTTP_OK
    assert b"Your Cart" in response.data
    assert product["name"].encode() in response.data


def test_remove_from_cart(client):
    """Test removing an item from the cart."""
    client.get("/add/1")
    response = client.get("/remove/1", follow_redirects=True)

    assert response.status_code == HTTP_OK
    assert b"Your Cart" in response.data
    assert b"Your cart is empty" in response.data


def test_checkout_with_items(client):
    """Test checking out clears the cart and shows a message."""
    client.get("/add/1")
    response = client.get("/checkout")

    assert response.status_code == HTTP_OK
    assert b"Thank you for your purchase" in response.data
    assert b"Your cart is empty" in response.data


def test_health_endpoint(client):
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == HTTP_OK
    assert response.json == {"status": "healthy"}


# Promo Code Tests
def test_valid_promo_code_winter25(client):
    """Test applying valid WINTER25 promo code (25% discount)."""
    product = next(p for p in PRODUCTS if p["id"] == 1)
    discount_rate = PROMO_CODES["WINTER25"]

    client.get("/add/1")
    response = client.post(
        "/cart", data={"promo_code": "winter25"}, follow_redirects=True
    )

    expected_total = product["price"]
    expected_discount = round(expected_total * discount_rate, 2)
    expected_discounted = round(expected_total - expected_discount, 2)

    assert response.status_code == HTTP_OK
    assert b"Promo code WINTER25 applied!" in response.data
    assert f"${expected_discounted:.2f}".encode() in response.data
    assert f"${expected_discount:.2f}".encode() in response.data


def test_valid_promo_code_welcome10(client):
    """Test applying valid WELCOME10 promo code (10% discount)."""
    product = next(p for p in PRODUCTS if p["id"] == 2)
    discount_rate = PROMO_CODES["WELCOME10"]

    client.get("/add/2")
    response = client.post(
        "/cart", data={"promo_code": "welcome10"}, follow_redirects=True
    )

    expected_total = product["price"]
    expected_discount = round(expected_total * discount_rate, 2)
    expected_discounted = round(expected_total - expected_discount, 2)

    assert response.status_code == HTTP_OK
    assert b"Promo code WELCOME10 applied!" in response.data
    assert f"${expected_discounted:.2f}".encode() in response.data


def test_invalid_promo_code(client):
    """Test applying invalid promo code."""
    product = next(p for p in PRODUCTS if p["id"] == 1)

    client.get("/add/1")
    response = client.post(
        "/cart", data={"promo_code": "INVALID"}, follow_redirects=True
    )

    assert response.status_code == HTTP_OK
    assert b"Invalid promo code" in response.data
    # Total should remain unchanged
    assert f"${product['price']:.2f}".encode() in response.data


def test_promo_code_persists_across_requests(client):
    """Test that promo code persists in session across requests."""
    product = next(p for p in PRODUCTS if p["id"] == 1)
    discount_rate = PROMO_CODES["WINTER25"]
    expected_discounted = round(product["price"] * (1 - discount_rate), 2)

    client.get("/add/1")
    client.post("/cart", data={"promo_code": "winter25"})
    response = client.get("/cart")

    assert response.status_code == HTTP_OK
    # Code should still be applied
    assert f"${expected_discounted:.2f}".encode() in response.data
    assert b"WINTER25" in response.data


def test_checkout_with_promo_code(client):
    """Test checkout displays discounted total."""
    product = next(p for p in PRODUCTS if p["id"] == 1)
    discount_rate = PROMO_CODES["WINTER25"]
    expected_discounted = round(product["price"] * (1 - discount_rate), 2)

    client.get("/add/1")
    client.post("/cart", data={"promo_code": "winter25"})
    response = client.get("/checkout")

    assert response.status_code == HTTP_OK
    assert (
        f"Thank you for your purchase! Total: ${expected_discounted:.2f}".encode()
        in response.data
    )
    assert b"Your cart is empty" in response.data
