import random
import pytest
from utils.api_helpers import get_cheapest_product

def test_add_cheapest_product_to_cart(session, base_url):
    """
    User Story 1:
    As an online shopper, I want to view all available products and add the cheapest item
    from a specific category to my cart.

    Acceptance Criteria:
    - The product must belong to a specific category (chosen as 'electronics').
    - Only products that are in stock (inferred via non-zero rating count).
    - Once added to the cart, the product should appear with correct quantity and product ID.

    Notes:
    - FakeStoreAPI does not persist cart state.
    - API response is trusted to reflect the simulated cart contents.
    """
    category = "electronics"  # could be randomised from a list of categories, but user story specifies electronics

    response = session.get(f"{base_url}/products/category/{category}")
    assert response.status_code == 200

    products = response.json()
    if not products:
        raise AssertionError(f"No products found in category '{category}'")

    cheapest_product = get_cheapest_product(products)
    assert cheapest_product, f"No products found in category '{category} that are in stock'"

    payload = {
        "userId": 1,
        "date": "2024-01-01",
        "products": [{"productId": cheapest_product["id"], "quantity": 1}]
    }

    cart_response = session.post(f"{base_url}/carts", json=payload)
    assert cart_response.status_code == 200
    cart = cart_response.json()

    assert cart["products"][0]["productId"] == cheapest_product["id"]
    assert cart["products"][0]["quantity"] == 1
