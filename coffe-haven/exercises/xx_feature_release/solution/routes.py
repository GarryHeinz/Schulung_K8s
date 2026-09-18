import uuid
from typing import Any

from flask import abort, redirect, render_template, request, session, url_for

PRODUCTS: list[dict[str, Any]] = [
    {
        "id": 1,
        "name": "Espresso Machine",
        "price": 899.99,
        "description": "Professional-grade equipment for the perfect home setup",
        "category": "equipment",
    },
    {
        "id": 2,
        "name": "Pour-Over Coffee Maker",
        "price": 49.99,
        "description": "Craft the perfect cup with precision and style",
        "category": "equipment",
    },
    {
        "id": 3,
        "name": "French Press",
        "price": 39.99,
        "description": "Classic brewing method for rich, full-bodied coffee",
        "category": "equipment",
    },
    {
        "id": 4,
        "name": "Coffee Grinder",
        "price": 129.99,
        "description": "Professional-grade burr grinder for consistent results",
        "category": "equipment",
    },
    {
        "id": 5,
        "name": "Milk Frother",
        "price": 29.99,
        "description": "Create silky smooth microfoam for your lattes",
        "category": "equipment",
    },
    {
        "id": 6,
        "name": "Cold Brew Maker",
        "price": 59.99,
        "description": "Brew smooth, low-acid coffee concentrate",
        "category": "equipment",
    },
    {
        "id": 7,
        "name": "Reusable Coffee Cup",
        "price": 19.99,
        "description": "Eco-friendly cup for coffee on the go",
        "category": "lifestyle",
    },
    {
        "id": 8,
        "name": "Coffee Bean Sampler Pack",
        "price": 34.99,
        "description": "Explore our curated selection of premium beans",
        "category": "beans",
    },
    {
        "id": 9,
        "name": "Single-Origin Espresso Beans",
        "price": 24.99,
        "description": "Carefully sourced beans for exceptional espresso",
        "category": "beans",
    },
    {
        "id": 10,
        "name": "Decaf Coffee Blend",
        "price": 21.99,
        "description": "Full flavor without the caffeine",
        "category": "beans",
    },
    {
        "id": 11,
        "name": "Matcha Latte Powder",
        "price": 27.99,
        "description": "Premium grade matcha for perfect lattes",
        "category": "lifestyle",
    },
    {
        "id": 12,
        "name": "Coffee Syrup Set (Vanilla, Caramel, Hazelnut)",
        "price": 18.99,
        "description": "Enhance your coffee with artisanal flavors",
        "category": "lifestyle",
    },
    {
        "id": 13,
        "name": "Barista Apron",
        "price": 34.99,
        "description": "Professional-grade barista essential",
        "category": "lifestyle",
    },
    {
        "id": 14,
        "name": "Latte Art Pitcher",
        "price": 22.99,
        "description": "Perfect pour control for latte art",
        "category": "equipment",
    },
    {
        "id": 15,
        "name": "Coffee Scented Candle",
        "price": 14.99,
        "description": "Bring the coffee shop atmosphere home",
        "category": "lifestyle",
    },
]

PROMO_CODES: dict[str, float] = {
    "WINTER25": 0.25,  # 25% discount
    "WELCOME10": 0.10,  # 10% discount
}

CARTS: dict[str, dict[str, Any]] = {}


def init_routes(app):
    def get_session_id() -> str:
        if "session_id" not in session:
            session["session_id"] = str(uuid.uuid4())
        return session["session_id"]

    def get_cart_state(session_id: str) -> dict[str, Any]:
        if session_id not in CARTS:
            CARTS[session_id] = {"items": [], "next_id": 1, "promo_code": None}
        return CARTS[session_id]

    def find_product(product_id: int) -> dict[str, Any]:
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if not product:
            abort(404, description="Product not found")
        return product

    def cart_total(items: list[dict[str, Any]]) -> float:
        return sum(item["quantity"] * item["product"]["price"] for item in items)

    def apply_discount(total: float, promo_code: str | None) -> tuple[float, float]:
        """Apply promo code discount if valid. Returns (discounted_total, discount_amount)"""
        if promo_code and promo_code in PROMO_CODES:
            discount_rate = PROMO_CODES[promo_code]
            discount_amount = total * discount_rate
            return round(total - discount_amount, 2), round(discount_amount, 2)
        return total, 0.0

    @app.route("/")
    def index():
        active_category = request.args.get("category", "all")
        available_categories = [
            {"slug": "all", "label": "All"},
            {"slug": "equipment", "label": "Equipment"},
            {"slug": "beans", "label": "Beans"},
            {"slug": "lifestyle", "label": "Lifestyle"},
        ]
        category_slugs = {cat["slug"] for cat in available_categories}
        if active_category not in category_slugs:
            active_category = "all"

        filtered_products = (
            PRODUCTS
            if active_category == "all"
            else [p for p in PRODUCTS if p.get("category") == active_category]
        )

        return render_template(
            "index.html",
            products=filtered_products,
            categories=available_categories,
            active_category=active_category,
        )

    @app.route("/cart", methods=["GET", "POST"])
    def cart():
        session_id = get_session_id()
        cart_state = get_cart_state(session_id)
        items = cart_state["items"]
        message = None

        if request.method == "POST":
            promo_code = request.form.get("promo_code", "").upper().strip()
            if promo_code in PROMO_CODES:
                cart_state["promo_code"] = promo_code
                message = f"Promo code {promo_code} applied!"
            elif promo_code:
                message = "Invalid promo code. Try WINTER25 or WELCOME10."

        total = cart_total(items)
        discounted_total, discount_amount = apply_discount(
            total, cart_state.get("promo_code")
        )

        return render_template(
            "cart.html",
            cart=items,
            message=message,
            total=total,
            discounted_total=discounted_total,
            discount_amount=discount_amount,
            promo_code=cart_state.get("promo_code"),
        )

    @app.route("/add/<int:product_id>")
    def add(product_id: int):
        session_id = get_session_id()
        cart_state = get_cart_state(session_id)
        product = find_product(product_id)

        cart_state["items"].append(
            {
                "id": cart_state["next_id"],
                "product": product,
                "quantity": 1,
            }
        )
        cart_state["next_id"] += 1
        return redirect(url_for("cart"))

    @app.route("/remove/<int:item_id>")
    def remove(item_id: int):
        session_id = get_session_id()
        cart_state = get_cart_state(session_id)
        items = cart_state["items"]
        cart_state["items"] = [item for item in items if item["id"] != item_id]
        return redirect(url_for("cart"))

    @app.route("/checkout")
    def checkout():
        session_id = get_session_id()
        cart_state = get_cart_state(session_id)
        items = cart_state["items"]

        if not items:
            return render_template(
                "cart.html",
                cart=[],
                message="Cart is empty",
                total=0.0,
                discounted_total=0.0,
                discount_amount=0.0,
                promo_code=None,
            )

        total = cart_total(items)
        discounted_total, _ = apply_discount(total, cart_state.get("promo_code"))
        cart_state["items"] = []
        cart_state["promo_code"] = None

        return render_template(
            "cart.html",
            cart=[],
            message=f"Thank you for your purchase! Total: ${discounted_total:.2f}",
            total=0.0,
            discounted_total=0.0,
            discount_amount=0.0,
            promo_code=None,
        )

    @app.route("/health")
    def health():
        return {"status": "healthy"}
