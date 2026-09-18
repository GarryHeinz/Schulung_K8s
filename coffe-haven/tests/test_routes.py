from app.routes import PRODUCTS

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
